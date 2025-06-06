from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import JsonResponse
from PIL import Image
import pytesseract
import re
from io import BytesIO
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from .models import Transaction
from .forms import TransactionForm

# Dashboard view (uses dashboard.html)
def dashboard(request):
    transaction_type = request.GET.get('type')
    if transaction_type in ['income', 'expense']:
        transactions = Transaction.objects.filter(transaction_type=transaction_type).order_by('-date')
    else:
        transactions = Transaction.objects.all().order_by('-date')

    total_income = Transaction.objects.filter(transaction_type='income').aggregate(total=Sum('amount'))['total'] or 0
    total_expense = Transaction.objects.filter(transaction_type='expense').aggregate(total=Sum('amount'))['total'] or 0
    balance = total_income - total_expense

    return render(request, 'dashboard.html', {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance
    })

# Add transaction view (uses add_transaction.html)
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to dashboard after saving
    else:
        form = TransactionForm()

    return render(request, 'add_transaction.html', {'form': form})

# Export transactions as PDF
def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="transactions.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    y = height - 50

    p.setFont("Helvetica-Bold", 14)
    p.drawString(200, y, "Transaction Report")
    y -= 30

    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, "Date")
    p.drawString(150, y, "Type")
    p.drawString(250, y, "Amount")
    p.drawString(350, y, "Description")
    y -= 20

    p.setFont("Helvetica", 10)
    for tx in Transaction.objects.all():
        if y < 50:
            p.showPage()
            y = height - 50
        p.drawString(50, y, tx.date.strftime("%Y-%m-%d"))
        p.drawString(150, y, tx.transaction_type.title())
        p.drawString(250, y, f"{tx.amount}")
        p.drawString(350, y, tx.description[:40])
        y -= 20

    p.save()
    return response
def ajax_receipt_ocr(request):
    if request.method == 'POST' and request.FILES.get('receipt'):
        receipt = request.FILES['receipt']
        image = Image.open(receipt)
        ocr_text = pytesseract.image_to_string(image)

        # Extract amount
        amount_match = re.search(r'(\d+\.\d{2})', ocr_text)
        amount = amount_match.group(1) if amount_match else ''

        # Extract description
        desc_match = re.search(r'(Item|Description|Desc):?\s*(.+)', ocr_text, re.IGNORECASE)
        description = desc_match.group(2).strip() if desc_match else ocr_text[:100]

        return JsonResponse({
            'amount': amount,
            'description': description
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
from django.db.models import Sum
from .models import Transaction

def dashboard(request):
    transactions = Transaction.objects.all()

    # Optional filter
    tx_type = request.GET.get('type')
    if tx_type:
        transactions = transactions.filter(transaction_type__iexact=tx_type)

    total_income = transactions.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transactions.filter(transaction_type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense  # This is your profit

    return render(request, 'dashboard.html', {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance
    })

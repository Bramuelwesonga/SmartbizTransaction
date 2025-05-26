from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'transaction_type', 'amount', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'transaction_type': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'date': 'Transaction Date',
            'transaction_type': 'Type',
            'amount': 'Amount',
            'description': 'Description (optional)',
        }
        help_texts = {
            'date': 'Select the date of the transaction.',
            'transaction_type': 'Choose whether this is an income or expense.',
            'amount': 'Enter the amount in your local currency.',
            'description': 'Optional notes about the transaction.',
        }
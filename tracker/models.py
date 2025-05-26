from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# This model represents a financial transaction (either income or expense)
class Transaction(models.Model):
    # Choices for transaction type - restricts input to either 'income' or 'expense'
    TYPE_CHOICES = [('income', 'Income'), ('expense', 'Expense')]

    # Field to store the type of transaction
    transaction_type = models.CharField(
        max_length=10,               # Max length of 10 characters
        choices=TYPE_CHOICES        # Limit choices to 'income' or 'expense'
    )

    # Field to store the amount of money for the transaction
    amount = models.DecimalField(
        max_digits=10,              # Total number of digits (e.g., 12345678.90)
        decimal_places=2            # Number of digits after the decimal point
    )

    # Field to store an optional description or notes for the transaction
    description = models.TextField(
        blank=True                  # Field is optional (can be empty)
    )

    # Automatically set the date when the transaction is created
    date = models.DateField(
        default=timezone.now       # Automatically uses current date
    )

    # Optional image field to upload a receipt or photo proof of the transaction
    receipt_image = models.ImageField(
        upload_to='receipts/',      # Uploaded files go into MEDIA_ROOT/receipts/
        null=True,                  # Field can be NULL in the database
        blank=True                  # Field is optional in forms
    )

    # Human-readable string representation of the model
    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"

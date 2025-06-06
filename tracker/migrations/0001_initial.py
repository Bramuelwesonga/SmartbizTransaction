# Generated by Django 5.0.6 on 2025-05-26 12:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('receipt_image', models.ImageField(blank=True, null=True, upload_to='receipts/')),
            ],
        ),
    ]

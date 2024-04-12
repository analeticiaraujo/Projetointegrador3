import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from models import Bills, Payment, Client

def create_invoice(client_id, received_value):
    try:
        client = Client.objects.get(id=client_id)
        bills = Bills.objects.create(client=client, amount=received_value)
        return bills
    except Client.DoesNotExist:
        print("Client with the specified ID does not exist.")
    except Exception as e:
        print("Error occurred while creating invoice:", e)

def record_payment(payment_id, value):
    try:
        # Fetch the invoice object
        bills = Bills.objects.get(id=payment_id)
        # Calculate the remaining amount after payment
        remaining_amount = Bills.amount - amount
        # Update is_paid status if remaining amount is zero or negative
        if remaining_amount <= 0:
            Bills.is_paid = True
        Bills.save()
        # Record the payment for the invoice
        payment = Payment.objects.create(invoice=payment_id, amount=amount)
        return payment
    except Bills.DoesNotExist:
        print("Invoice with the specified ID does not exist.")
    except Exception as e:
        print("Error occurred while recording payment:", e)

def generate_report():
    try:
        # Retrieve all invoices and payments
        invoices = Bills.objects.all()
        payments = Payment.objects.all()
        # Perform report generation logic here
        # Example:
        report_data = {
            "invoices": invoices,
            "payments": payments
            # Add more data to the report as needed
        }
        return report_data
    except Exception as e:
        print("Error occurred while generating report:", e)
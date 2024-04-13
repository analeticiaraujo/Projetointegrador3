import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from models import BillPayment, EntryValue, ClientRegistration

def create_invoice(client_id, received_value):
    try:
        client = ClientRegistration.objects.get(id=client_id)
        bills = BillPayment.objects.create(client=client, amount=received_value)
        return bills
    except ClientRegistration.DoesNotExist:
        print("Client with the specified ID does not exist.")
    except Exception as e:
        print("Error occurred while creating invoice:", e)

def record_payment(payment_id, amount):
    try:
        # Fetch the invoice object
        bills = BillPayment.objects.get(id=payment_id)
        # Calculate the remaining amount after payment
        remaining_amount = BillPayment.amount - amount
        # Update is_paid status if remaining amount is zero or negative
        if remaining_amount <= 0:
            BillPayment.is_paid = True
        BillPayment.save()
        # Record the payment for the invoice
        payment = EntryValue.objects.create(invoice=payment_id, amount=amount)
        return payment
    except BillPayment.DoesNotExist:
        print("Invoice with the specified ID does not exist.")
    except Exception as e:
        print("Error occurred while recording payment:", e)

def generate_report():
    try:
        # Retrieve all invoices and payments
        invoices = BillPayment.objects.all()
        payments = EntryValue.objects.all()
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
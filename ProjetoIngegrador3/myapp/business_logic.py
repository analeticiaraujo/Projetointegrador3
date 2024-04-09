import os
import django
from django.conf import settings


# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

# Import Django models after setup
from models import Invoice, Payment, Client

def create_invoice(client_id, amount):
    try:
        # Fetch the client object
        client = Client.objects.get(id=client_id)
        # Create an invoice for the client with the specified amount
        invoice = Invoice.objects.create(client=client, amount=amount)
        return invoice
    except Client.DoesNotExist:
        print("Client with the specified ID does not exist.")
    except Exception as e:
        print("Error occurred while creating invoice:", e)

def record_payment(invoice_id, amount):
    try:
        # Fetch the invoice object
        invoice = Invoice.objects.get(id=invoice_id)
        # Calculate the remaining amount after payment
        remaining_amount = invoice.amount - amount
        # Update is_paid status if remaining amount is zero or negative
        if remaining_amount <= 0:
            invoice.is_paid = True
        invoice.save()
        # Record the payment for the invoice
        payment = Payment.objects.create(invoice=invoice, amount=amount)
        return payment
    except Invoice.DoesNotExist:
        print("Invoice with the specified ID does not exist.")
    except Exception as e:
        print("Error occurred while recording payment:", e)

def generate_report():
    try:
        # Retrieve all invoices and payments
        invoices = Invoice.objects.all()
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
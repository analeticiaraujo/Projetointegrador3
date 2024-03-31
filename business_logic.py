from models import Invoice, Payment

def create_invoice(client_id, amount):
    # Business logic to create an invoice
    # Example:
    client = Client.objects.get(id=client_id)
    invoice = Invoice.objects.create(client=client, amount=amount)
    return invoice

def record_payment(invoice_id, amount):
    # Business logic to record a payment for an invoice
    # Example:
    invoice = Invoice.objects.get(id=invoice_id)
    remaining_amount = invoice.amount - amount
    if remaining_amount <= 0:
        invoice.is_paid = True
    invoice.save()
    payment = Payment.objects.create(invoice=invoice, amount=amount)
    return payment

def generate_report():
    # Business logic to generate a financial report
    # Example:
    invoices = Invoice.objects.all()
    payments = Payment.objects.all()
    # Generate report logic here
    return report_data
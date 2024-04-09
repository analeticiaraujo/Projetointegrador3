from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Invoice, Payment, Client

@login_required
def create_invoice(request):
    if request.method == 'POST':
        # Logic to create an invoice
        return JsonResponse({'message': 'Invoice created successfully'})
    else:
        # Render the form to create an invoice
        return render(request, 'create_invoice.html')

@login_required
def record_payment(request):
    if request.method == 'POST':
        # Logic to record a payment
        return JsonResponse({'message': 'Payment recorded successfully'})
    else:
        # Render the form to record a payment
        return render(request, 'record_payment.html')

@login_required
def generate_report(request):
    # Logic to generate financial report
    return render(request, 'report.html')

@login_required
def view_invoice(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    # Check if the user has permission to view this invoice
    if not request.user.has_perm('app.view_invoice') or (invoice.client != request.user and not request.user.is_superuser):
        return render(request, 'access_denied.html')
    # Render the invoice template
    return render(request, 'invoice.html', {'invoice': invoice})

@login_required
@permission_required('app.add_invoice')
def create_invoice(request):
    if request.method == 'POST':
        # Logic to create invoice
        pass
    else:
        # Render the form to create an invoice
        return render(request, 'create_invoice.html')
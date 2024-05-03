from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from myapp.models import ClientRegistration, BillPayment, EntryValue
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.models import User


def pagina_inicial(request):
    return HttpResponse('Hello, World!')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user directly with the provided credentials
        user = authenticate(request, username=username, password=password)
        print(f'{user}')
        if user is not None:
            login(request, user)
            print(f"User {username} logged in successfully.")
            # Redirect to the appropriate page after successful login
            return redirect('relatorios.html')  # Replace 'relatorios' with your desired URL
        
        # If authentication fails, show an error message
        return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')
    
    
def pagina_cadastro_clientes(request):
    if request.method == 'POST':
        if 'edit_id' in request.POST:
            # Editing existing client data
            registration_id = request.POST.get('edit_id')
            client = ClientRegistration.objects.get(pk=registration_id)
            client.client = request.POST.get('client')
            client.client_type = request.POST.get('client_type')
            client.identifier = request.POST.get('identifier')
            client.legal_action = request.POST.get('legal_action')
            client.save()
            return render(request, 'cadastro_clientes.html', {'editing': True})
        elif 'delete_id' in request.POST:
            # Deleting client data
            delete_id = request.POST.get('delete_id')
            client = ClientRegistration.objects.get(pk=delete_id)
            client.delete()
            return render(request, 'cadastro_clientes.html', {'deleting': True})
        else:
            # Registering new client
            client = ClientRegistration(
                client=request.POST.get('client'),
                client_type=request.POST.get('client_type'),
                identifier=request.POST.get('identifier'),
                legal_action=request.POST.get('legal_action')
            )
            client.save()
            return redirect('cadastro_clientes')  # Redirect to avoid form resubmission
    else:
        # Render the client page without editing mode
        clients = ClientRegistration.objects.all()
        return render(request, 'cadastro_clientes.html', {'clients': clients})
    
    
def pagina_recebimentos_e_despesas(request):
    # Consulta ao banco de dados para obter os pagamentos de contas e valores recebidos
    bill_payments = BillPayment.objects.all()
    entry_values = EntryValue.objects.all()
    clients = ClientRegistration.objects.all()
    
    context = {
        'bill_payments': bill_payments,
        'entry_values': entry_values,
        'clients': clients
    }
    return render(request, 'recebimentosedespesas.html', context)


def pagina_relatorios(request):
    clients = ClientRegistration.objects.all()
    
    # Obter todos os valores recebidos
    entries = EntryValue.objects.all()
    
    # Obter todos os pagamentos de contas
    payments = BillPayment.objects.all()
    
    return render(request, 'relatorios.html', {'clients': clients, 'entries': entries, 'payments': payments})


def handle_integrity_error(e):
    # Extract more specific error details from the exception
    error_message = str(e)  # Replace with more specific logic if needed
    return HttpResponse(f"Error occurred while saving user data: {error_message}")

def pagina_edicao_usuario(request, user_id=None):
    if user_id is not None:
        user = get_object_or_404(User, id=user_id)
    else:
        user = User()
    if request.method == 'POST':
        if 'delete' in request.POST:
            # Delete the user if 'delete' button is clicked
            try:
                user.delete()
            except Exception as e:
                return HttpResponse("Error occurred while deleting user: " + str(e))
            return redirect('user_list')  # Redirect to the user list page after deletion
        else:
            # Update the user data
            username = request.POST.get('username')
            password = request.POST.get('password')
            if not username or not password:  # Check if username or password is empty
                return HttpResponse("Username and password are required.")
            # Check if the provided username belongs to the current user
            if username != user.username:
                # Check if the new username already exists
                if User.objects.filter(username=username).exists():
                    return HttpResponse("Username already exists. Please choose a different username.")
            # Update password and level
            user.username = username
            user.set_password(password)  # Use set_password to hash the password
            user.level = request.POST.get('level')

            try:
                user.save()
                if user_id is None:
                    return HttpResponse("User created with success!")
                else:
                    return redirect('user_detail', user_id=user.id)  # Redirect to user detail page after edit or creation
            except IntegrityError as e:
                return handle_integrity_error(e)

    context = {'users': User.objects.all(), 'user': user}  # Fetch all users for the form
    return render(request, 'edicao_usuario.html', context)

def pagina_logout(request):
    logout(request)
    return redirect('login')
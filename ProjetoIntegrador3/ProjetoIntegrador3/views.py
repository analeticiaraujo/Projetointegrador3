from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from myapp.models import ClientRegistration, BillPayment, EntryValue 
from django.contrib.auth.models import User
from django.contrib.auth import logout

def pagina_inicial(request):
    return HttpResponse('Hello, World!')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if user.stored_password == password:
                # Authentication successful
                # Redirect to a specific URL after login, or to a default one
                return redirect('relatorios')  # Replace 'dashboard' with your desired URL name
            else:
                error_message = "Invalid username or password"
                return render(request, 'login.html', {'error_message': error_message})
        except User.DoesNotExist:
            error_message = "Usuário não encontrado"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def pagina_cadastro_clientes(request):
    if request.method == 'POST':
        if 'registration_id' in request.POST:
            # Editing existing client data
            registration_id = request.POST.get('registration_id')
            client = ClientRegistration.objects.get(pk=registration_id)
            client.client = request.POST.get('client')
            client.client_type = request.POST.get('client_type')
            client.identifier = request.POST.get('identifier')
            client.save()
            return render(request, 'client_page.html', {'editing': False})  # Render the client page without editing mode
        else:
            # Registering new client
            client = ClientRegistration(
                client=request.POST.get('client'),
                client_type=request.POST.get('client_type'),
                identifier=request.POST.get('identifier')
            )
            client.save()
            return render(request, 'cadastro_clientes.html', {'registration_id': client.registration_id})
    else:
        # Render the client page without editing mode
        return render(request, 'cadastro_clientes.html', {'editing': False})

def pagina_recebimentos_e_despesas(request):
    # Consulta ao banco de dados para obter os pagamentos de contas e valores recebidos
    bill_payments = BillPayment.objects.all()
    entry_values = EntryValue.objects.all()

    context = {
        'bill_payments': bill_payments,
        'entry_values': entry_values
    }
    return render(request, 'recebimentosedespesas.html', context)


def pagina_relatorios(request):
    clients = ClientRegistration.objects.all()
    
    # Obter todos os valores recebidos
    entries = EntryValue.objects.all()
    
    # Obter todos os pagamentos de contas
    payments = BillPayment.objects.all()
    
    return render(request, 'relatorios.html', {'clients': clients, 'entries': entries, 'payments': payments})

def pagina_edicao_usuario(request, user_id=None):
    if user_id is not None:
        user = get_object_or_404(User, id=user_id)
    else:
        user = User()  # Create a new user instance if user_id is not provided

    if request.method == 'POST':
        if 'delete' in request.POST:
            # Delete the user if 'delete' button is clicked
            user.delete()
            return redirect('user_list')  # Redirect to the user list page after deletion
        else:
            # Update the user data if it's an existing user, or create a new user
            user.username = request.POST.get('username')
            user.set_password(request.POST.get('password'))  # Use set_password to hash the password
            user.level = request.POST.get('level')
            user.save()
            return redirect('user_detail', user_id=user.id)  # Redirect to user detail page after edit or creation
    return render(request, 'edicao_usuario.html', {'user': user})

def pagina_logout(request):
    logout(request)
    return redirect('login')
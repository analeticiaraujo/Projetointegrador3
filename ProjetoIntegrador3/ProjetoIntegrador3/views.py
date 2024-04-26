from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

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
                return redirect('dashboard')  # Replace 'dashboard' with your desired URL name
            else:
                error_message = "Invalid username or password"
                return render(request, 'login.html', {'error_message': error_message})
        except User.DoesNotExist:
            error_message = "Usuário não encontrado"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def dashboard_view(request):
    # Check if the user is authenticated
    if 'user_id' not in request.session:
        return redirect('login')  # Redirect to login page if not authenticated
    
    # Example authorization
    # You might want to implement a more fine-grained authorization mechanism
    user_id = request.session['user_id']
    user = User.objects.get(pk=user_id)
    if not user.has_access(required_level=2):
        return redirect('unauthorized')  # Redirect to unauthorized page if access level is insufficient
    
    # Render dashboard page if authenticated and authorized
    return render(request, 'dashboard.html')

def pagina_cadastro_clientes(request):
    return HttpResponse('Inserir dados dos clientes')

def pagina_recebimentos_e_despesas(request):
    return HttpResponse('Inserir dados de recebimentos e despesas e gerar relatórios')

def pagina_relatorios(request):
    return HttpResponse('Gerar relatórios')

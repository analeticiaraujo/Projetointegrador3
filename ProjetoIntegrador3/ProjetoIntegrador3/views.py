from django.shortcuts import render, HttpResponse

def pagina_inicial(request):
    return HttpResponse('Hello, World!')

def pagina_login(request):
    return HttpResponse('Hello, World!')

def pagina_cadastro_clientes(request):
    return HttpResponse('Inserir dados dos clientes')

def pagina_recebimentos_e_despesas(request):
    return HttpResponse('Inserir dados de recebimentos e despesas e gerar relatórios')

def pagina_relatorios(request):
    return HttpResponse('Gerar relatórios')

from django.shortcuts import render, HttpResponse

def pagina_inicial(request):
    return HttpResponse('Hello, World!')

def pagina_login(request):
    return HttpResponse('Hello, World!')
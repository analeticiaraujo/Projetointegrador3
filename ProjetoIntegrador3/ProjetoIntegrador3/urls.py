"""
URL configuration for ProjetoIngegrador3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='paginaInicial'),
    path('login/', views.login_view, name='paginaLogin'),
    path('cadastro_clientes/', views.pagina_cadastro_clientes, name='paginaCadastroClientes'),
    path('recebimentos_e_despesas/', views.pagina_recebimentos_e_despesas, name='paginaRecebimentosDespesas'),
    path('relatorios/', views.pagina_relatorios, name='paginaRelatorios'),
    path('edicao_usuario/', views.pagina_edicao_usuario, name='paginaEdicaoUsuario'),
    path('logout/', views.pagina_logout, name='paginaLogout'),
    path('admin/', admin.site.urls)

]
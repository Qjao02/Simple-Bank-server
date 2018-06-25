from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from bankserverapp.views import ClienteView, ClienteListView, FuncionarioListView,FuncionarioView,AdministradorView,AdministradorListView


helper_patterns = [
    
    url(r'v1/Clientes/$', ClienteListView.as_view(), name = 'ClientListView'),
    url(r'v1/Clientes/(?P<pk>[0-9]+)$', ClienteView.as_view(), name = 'ClientView'),
    url(r'v1/Funcionarios/$', FuncionarioListView.as_view(), name = 'FuncionarioListView'),
    url(r'v1/Funcionarios/(?P<pk>[0-9]+)$', FuncionarioView.as_view(), name = 'FuncionarioView'),
    url(r'v1/Administradores/$', AdministradorListView.as_view(), name = 'AdministradorListView'),
    url(r'v1/Administradores/(?P<pk>[0-9]+)$', AdministradorView.as_view(), name = 'AdministradorView')
]
urlpatterns = helper_patterns
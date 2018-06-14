from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from bankserverapp.views import ClienteView
from bankserverapp.views import ClienteListView


helper_patterns = [
    
    url(r'v1/Clientes/$', ClienteListView.as_view(), name = 'ClientListView'),
    url(r'v1/Clientes/(?P<pk>[0-9]+)$', ClienteView.as_view(), name = 'ClientView')
]
urlpatterns = helper_patterns
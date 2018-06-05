from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from bankserverapp.views import ClienteView


helper_patterns = [
    
    url('v1/Clientes/', ClienteView.as_view, name = 'Clientes'),

]
urlpatterns = helper_patterns
from django.shortcuts import render
from .serializer import ClienteSerializer
from .models import Cliente


from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ClienteView(APIView):

    serializer_class = ClienteSerializer

    def get(self, request, format = None):
        serializer = self.serializer_class(Cliente, many = True)
            
        return Response(serializer.data)

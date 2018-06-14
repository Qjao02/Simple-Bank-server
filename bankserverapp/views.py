from django.shortcuts import render

from .serializer import ClienteSerializer
from .models import Cliente

from collections import namedtuple
from django.db.models.query import RawQuerySet
from django.db  import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json 

# Create your views here.
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

class ClienteListView(APIView):

    serializer_class = ClienteSerializer

    def get(self, request,  format = None):
        print('foiget')
        cursor = connection.cursor()
        #response = dictfetchall(cursor)
        serializer = self.serializer_class(Cliente.objects.raw('SELECT * FROM bankserverapp_cliente'), many = True)

        
        return Response(serializer.data)

    def post(self,request, format = None):

        print ('foiPost')
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            
            cursor = connection.cursor()
            cursor.execute('INSERT INTO bankserverapp_cliente(cadastroDatetime, endereco, nome, origem_funcionario_id) VALUES(CURDATE(), "'+ serializer.data['endereco'] + '","'+ serializer.data['nome']+'", 1);')
            print('INSERT INTO bankserverapp_cliente(cadastroDatetime, endereco, nome, origem_funcionario_id) VALUES(CURDATE(), "'+ serializer.data['endereco'] + '","'+ serializer.data['nome']+'", 1);')

            return Response(serializer.data, status = status.HTTP_201_CREATED)

        else:
            return Response({"message" :"403 Forbidden"}, status = status.HTTP_409_CONFLICT)


class ClienteView(APIView):
    
    serializer_class = ClienteSerializer

    
    def delete(self, request, pk ,format=None):
       
        try:
            Cliente.objects.get(pk = pk)
            cursor = connection.cursor()
            cursor.execute('DELETE from bankserverapp_cliente where id = "'+pk+'";')
            return Response(status = status.HTTP_202_ACCEPTED)

        except:
            return Response(status = status.HTTP_204_NO_CONTENT)

    '''
    def put(self,request, pk, format=None):
        try:
            Cliente.objects.get(pk = pk):
            cursor.execute('UPDATE bankserverapp_cliente SET ')'''
'''
def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
'''
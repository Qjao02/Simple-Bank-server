from django.shortcuts import render

from .serializer import ClienteSerializer,FuncionarioSerializer, AdministradorSerializer
from .models import Cliente,Funcionario,Administrador

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
    print('called')
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
        print(serializer.initial_data)
        if serializer.is_valid():
            
            cursor = connection.cursor()
            cursor.execute('INSERT INTO bankserverapp_cliente(data_cadastro,nome,rua_mora,cidade_mora,estado_mora,funcionario_cadastrou) VALUES(NOW(), "' + serializer.data['nome'] +'","'+ serializer.data['rua_mora'] +'","' + serializer.data['cidade_mora'] +'","' + serializer.data['estado_mora'] + '","' + serializer.data['funcionario_cadastrou'] + '");')

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

    def put(self, request, pk ,format=None):
        user = Cliente.objects.raw('SELECT * FROM bankserverapp_cliente WHERE id="' + pk + '"')
        serializer = self.serializer_class(data=request.data)
        print(serializer.initial_data)

        if serializer.is_valid():
            upd = "UPDATE bankserverapp_cliente SET nome='" + serializer.data['nome'] + "', rua_mora = '" + serializer.data['rua_mora'] + "', cidade_mora = '" + serializer.data['cidade_mora'] + "', estado_mora = '" + serializer.data['estado_mora'] + "' WHERE id = " + str(pk) + ";"
            cursor = connection.cursor()
            cursor.execute(upd)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response({"message" :"403 Forbidden"}, status = status.HTTP_409_CONFLICT)



class FuncionarioView(APIView):
    serializer_class = FuncionarioSerializer

    def get(self, request, pk, format = None):
        slt = "SELECT * FROM bankserverapp_funcionario WHERE id='" + pk + "'"
        user = Funcionario.objects.raw(slt)
        cursor = connection.cursor()
        serializer = self.serializer_class(user, many = True)
        return Response(serializer.data)

    def delete(self, request, pk ,format=None):
        try:
            dlt = "DELETE from bankserverapp_funcionario where id = '" + pk + "';"
            cursor = connection.cursor()
            cursor.execute('DELETE from bankserverapp_funcionario where id = "' + pk + '";')
            return Response(status = status.HTTP_202_ACCEPTED)
        except:
            return Response(status = status.HTTP_204_NO_CONTENT)

    def put(self, request, pk ,format=None):
            user = Funcionario.objects.raw('SELECT * FROM bankserverapp_funcionario WHERE id="' + pk + '"')
            serializer = self.serializer_class(data=request.data)
            print(serializer.initial_data)
            if serializer.is_valid():
                upd = "UPDATE bankserverapp_funcionario SET login='" + serializer.data['login'] + \
                            "', senha='" + serializer.data['senha'] + "' WHERE id=" + pk + ";"
                cursor = connection.cursor()
                cursor.execute(upd)
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response({"message" :"403 Forbidden"}, status = status.HTTP_409_CONFLICT)

                
class FuncionarioListView(APIView):
    #Dados do funcionario a serem serializados
    serializer_class = FuncionarioSerializer
    #Método GET
    def get(self, request,  format = None):
        slt = 'SELECT * FROM bankserverapp_funcionario'
        cursor = connection.cursor()
        serializer = self.serializer_class(Funcionario.objects.raw(slt), many = True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            isrt = "INSERT INTO bankserverapp_funcionario(data_cadastro, senha, login, adm_cadastrou) \
                    VALUES(NOW(), '" + serializer.data['senha'] + "','" + serializer.data['login'] +"','" +  serializer.data['adm_cadastrou'] +  "');"
            cursor = connection.cursor()
            cursor.execute(isrt)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response({"message" :"403 Forbidden"}, status = status.HTTP_409_CONFLICT)

class AdministradorView(APIView):
    serializer_class = AdministradorSerializer

    def get(self, request, pk, format = None):
        slt = "SELECT * FROM bankserverapp_administrador WHERE id='" + pk + "'"
        user = Administrador.objects.raw(slt)
        cursor = connection.cursor()
        serializer = self.serializer_class(user, many = True)
        return Response(serializer.data)

    def delete(self, request, pk ,format=None):
        try:
            dlt = "DELETE from bankserverapp_administrador where id = '" + pk + "';"
            cursor = connection.cursor()
            cursor.execute('DELETE from bankserverapp_administrador where id = "' + pk + '";')
            return Response(status = status.HTTP_202_ACCEPTED)
        except:
            return Response(status = status.HTTP_204_NO_CONTENT)

    def put(self, request, pk ,format=None):
            user = Administrador.objects.raw('SELECT * FROM bankserverapp_administrador WHERE id="' + pk + '"')
            serializer = self.serializer_class(data=request.data)
            print(serializer.initial_data)
            if serializer.is_valid():
                upd = "UPDATE bankserverapp_administrador SET login='" + serializer.data['login'] + \
                            "', senha='" + serializer.data['senha'] + "' WHERE id=" + pk + ";"
                cursor = connection.cursor()
                cursor.execute(upd)
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response({"message" :"403 Forbidden"}, status = status.HTTP_409_CONFLICT)

                
class AdministradorListView(APIView):
    #Dados do funcionario a serem serializados
    serializer_class = AdministradorSerializer
    #Método GET
    def get(self, request,  format = None):
        slt = 'SELECT * FROM bankserverapp_administrador'
        cursor = connection.cursor()
        serializer = self.serializer_class(Administrador.objects.raw(slt), many = True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            isrt = "INSERT INTO bankserverapp_administrador(senha, login, agencia) \
                    VALUES('" + serializer.data['senha'] + "','" + serializer.data['login'] +"','" +  serializer.data['agencia'] +  "');"
            cursor = connection.cursor()
            cursor.execute(isrt)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response({"message" :"403 Forbidden"}, status = status.HTTP_409_CONFLICT)


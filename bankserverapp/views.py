from django.shortcuts import render

from .serializer import ClienteSerializer
from .models import Cliente

from collections import namedtuple
from django.db.models.query import RawQuerySet
from django.db  import connection
from rest_framework.views import APIView
from rest_framework.response import Response

import json 

# Create your views here.
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

class ClienteView(APIView):

    serializer_class = ClienteSerializer

    def get(self, request, format = None):

        cursor = connection.cursor()
        cursor.execute('SELECT * from cliente')
        response = dictfetchall(cursor)

        
            
        return Response(response)

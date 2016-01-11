from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Query
from .serializers import QuerySerializer

class QueryView(APIView):
    def get(self, request, format=None):
        q = request.GET.get('q', None)
        print 'QUERY:', q
        query = Query(q=q)
        serializer = QuerySerializer(query)
        return Response(serializer.data)

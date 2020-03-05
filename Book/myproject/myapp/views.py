# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from myapp.models import Book
from myapp.serializers import BookSerializer
from django.http import HttpResponse

@api_view(['GET', 'POST'])
def book_list(request):
    """
    POST, VIEW, UPDATE AND DELETE
    THE FIRST IF STATEMENT IS FOR GET FOLLOWED BY THE POST, UPDATE AND DELETE
    THIS HELPS THE USERS TO ACCES THE BOOK APPLICATION AND SERVES AS THE BACKEND OF THE BOOKS REPOSITORY
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import datetime
from .serializers import BookSerializer
from .models import Book
import pytz
from rest_framework.settings import api_settings

# Create your views here.

class BookView(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class =  BookSerializer

    def retrive(self, request, *args, **kwargs):
        
        requestBook = self.get_object()
        urlRequestTime = pytz.utc.localize(datetime.datetime.utcnow())

        if urlRequestTime > requestBook.expiry:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            requestBook.expiry = urlRequestTime + datetime.timedelta(seconds=60)
            requestBook.save()
            serializer = BookSerializer(requestBook)
            if serializer.data:
                return Response(serializer.data['book_text'])


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(request.build_absolute_uri()+str(serializer.data['id'])+"/", status=status.HTTP_201_CREATED, headers=headers)

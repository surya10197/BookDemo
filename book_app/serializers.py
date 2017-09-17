from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    bookName = serializers.CharField(source='name')
    book_text = serializers.CharField(source='content')

    class Meta:
        model = Book
        fields = ('id', 'bookName', 'author', 'book_text', 'created', 'expiry')

from rest_framework import serializers
from myapp.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('url', 'name', 'isbn', 'publisher_year', 'publisher_name', 'date_created', 'date_modified')



from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "name", "description", "count", "authors")


class BookListSerializer(BookSerializer):
    authors = serializers.SlugRelatedField(many=True, read_only=True, slug_field="surname")

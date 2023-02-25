from rest_framework import serializers
from author.models import Author
from api.book_api.serializers import BookSerializer


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("id", "name", "patronymic", "surname", "books")


class AuthorDetailSerializer(AuthorSerializer):
    books = BookSerializer(many=True, read_only=True)


class AuthorListSerializer(AuthorSerializer):
    books = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

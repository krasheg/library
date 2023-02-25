from rest_framework import viewsets

from api.book_api.serializers import BookSerializer, BookListSerializer
from book.models import Book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("-id")
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return BookListSerializer
        return BookSerializer

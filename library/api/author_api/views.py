from rest_framework import viewsets

from api.author_api.serializers import AuthorSerializer, AuthorListSerializer, AuthorDetailSerializer
from author.models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by("-id")
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action in ("list", "retrieve"):
            queryset = queryset.prefetch_related("books")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return AuthorListSerializer
        if self.action == "retrieve":
            return AuthorDetailSerializer
        return AuthorSerializer

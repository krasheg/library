from django.contrib import admin
from author.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    list_filter = ('name', 'surname', 'id')
    fields = [('name', 'surname'), 'patronymic', 'books']

    class Meta:
        model = Author
        model.__str__ = lambda x: f'{x.name} {x.surname}'


admin.site.register(Author, AuthorAdmin)

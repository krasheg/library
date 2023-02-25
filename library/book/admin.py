from django.contrib import admin
from book.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'count', 'book_authors')
    list_filter = ('id', 'name', 'authors')
    fieldsets = (
        ('DATA THAT DO NOT CHANGE', {'fields': ('name', 'year_of_publication', 'book_authors')}),
        ('DATA THAT CHANGE', {'fields': ('description', 'count', 'date_of_issue')}))
    readonly_fields = ['name', 'book_authors', 'year_of_publication']

    def book_authors(self, obj):
        return ', '.join([str(a) for a in obj.authors.all()])

    class Meta:
        model = Book
        model.__str__ = lambda x: x.name


admin.site.register(Book, BookAdmin)

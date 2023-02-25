from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Author
from book.models import Book


#
#
# class AuthorsList(View):
#     template_name = 'author/author_list.html'
#
#     def get(self, request):
#         authors = Author.objects.all()
#         context = {'authors': authors}
#         return render(request, 'author/author_list.html', context)
class AuthorsList(LoginRequiredMixin, ListView):
    model = Author

    def get_queryset(self):
        return Author.objects.all()


def delete_author(request, id):
    author = Author.get_by_id(id)
    books = [book for book in author.books.all()]
    if not books:
        Author.delete_by_id(id)
        authors = Author.get_all()
        return redirect('/authors')
    else:
        msg = 'Cannot delete author because he has books'
        authors = Author.get_all()
        return render(request, 'author/author_list.html', {'author_list': authors, 'msg': msg})


def create_author(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'author/create_author.html', {'books': books})
    if request.method == 'POST':
        # try:
        name = request.POST.get('author_name')
        surname = request.POST.get('last_name')
        patronymic = request.POST.get('middle_name')
        books = request.POST.getlist('books')
        author = Author.create(name, surname, patronymic)
        if books:
            for book_id in books:
                book = Book.objects.get(id=int(book_id))
                book.add_authors([author])
        return redirect('/authors')
        # except:
        #     messages.error(request, f'ERROR! Incorrect password!')
        #     return render(request, 'author/create_author.html')

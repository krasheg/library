from django.shortcuts import render, redirect
from .models import Book
from author.models import Author
from django.db.models import Q


def get_list_of_books(request):
    book = None
    msg = None
    if request.method == 'GET':
        books = Book.get_all()
        return render(request, 'book/book_list.html', {'book_list': books})
    if request.method == 'POST':
        book = None
        if 'by_book_id' in request.POST:
            try:
                book_id = int(request.POST.get('search'))
                book = [Book.get_by_id(book_id)]
            except:
                book = None
                msg = 'No books were found'
            if not book[0]:
                book = None
        elif 'by_book_title' in request.POST:
            try:
                title = request.POST.get('search')
                book = [i for i in Book.objects.filter(Q(name__icontains=title))]
            except:
                book = None
                msg = 'No books were found'
        elif 'by_book_description' in request.POST:
            try:
                description = request.POST.get('search')
                book = [i for i in Book.objects.filter(Q(description__icontains=description))]
            except:
                book = None
                msg = 'No books were found'
        elif 'by_user_id' in request.POST:
            try:
                user_id = int(request.POST.get('search'))
                book = [i for i in Book.objects.filter(Q(authors__in=[user_id]))]
            except:
                book = None
                msg = 'No books were found'
        return render(request, 'book/book_list.html', {'book_list': book, 'message': msg})


def create_book(request):
    if request.method == 'GET':
        books = Book.get_all()
        authors = Author.get_all()
        return render(request, 'book/create_book.html', {'book_list': books, 'authors': authors})
    if request.method == 'POST':
        name = request.POST.get('book_name')
        description = request.POST.get('description')
        count = request.POST.get('count')
        authors = request.POST.getlist('authors')
        print(name, description, count, authors)
        book = Book.create(name, description, count)
        if authors:
            authors = map(lambda x: Author.get_by_id(int(x)), authors)
            print(authors)
            book.add_authors(authors)
        return redirect('/book')


def delete_book(request, id):
    Book.delete_by_id(id)
    return get_list_of_books(request)

from django.shortcuts import render, redirect
from django.contrib import messages
from authentication.models import CustomUser
from order.models import Order
from book.models import Book
import datetime


def order(request):
    if not request.user.is_authenticated:
        return redirect('index/')
    orders = Order.get_all()
    if not request.user.role:
        if orders:
            result = []
            for order_ in orders:
                if order_.user.id == request.user.id:
                    result.append(order_)
            orders = result
    return render(request, 'order/order.html', {'orders': orders if orders else False})


def delete_order(request, id):
    Order.delete_by_id(id)
    return redirect('/order/', request=request)


def create(request):
    if not request.user.is_authenticated:
        return redirect('index/')

    if request.POST:
        date = request.POST['date']
        user = request.POST['user'].split('id:')[1]
        book = request.POST['book'].split('id:')[1]
        book = Book.get_by_id(int(book))
        user = CustomUser.get_by_id(int(user))
        orders = Order.create(user, book, date)
        print(request.user)
        if orders:
            messages.success(request, 'Done')
            return redirect('/order/', request=request)

        else:
            messages.success(request, 'Fail')
            books = Book.get_all()
            if request.user.is_staff or request.user.is_superuser:
                users = CustomUser.get_all()
            else:
                users = []
                users.append(request.user)
            return render(request, 'order/order.html')

    else:
        books = Book.get_all()
        if request.user.role:
            users = CustomUser.get_all()
        else:
            users = []
            users.append(request.user)
        return render(request, 'order/create.html', {'books': books, 'users': users})


def complete(request, id):
    if not request.user.is_authenticated:
        return redirect('index/')
    order_ = Order.get_by_id(id)
    if order_:
        order_.update(end_at=datetime.datetime.now())
        messages.success(request, 'Done')
    else:
        messages.error(request, 'Fails')

    return redirect('/order/', request=request)



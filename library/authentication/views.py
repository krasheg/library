from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from authentication.models import CustomUser


def index(request):
    return render(request, 'index.html')


def login_(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, f'ERROR! Incorrect password!')

        else:
            messages.error(request, f'ERROR! The user does not exist, please sign up!')

        return redirect("login")
    else:
        return render(request, 'authentication/login.html')


def register(request):
    if request.POST:
        for i in request.POST:
            if request.POST[i] == '':
                messages.error(request, f"{i} must be field")
                return HttpResponseRedirect(reverse('register'))
        a = CustomUser.create(email=request.POST['email'],
                              first_name=request.POST['user_name'],
                              last_name=request.POST['last_name'],
                              middle_name=request.POST['middle_name'],
                              password=""
                              )
        user = CustomUser.objects.get(email=request.POST['email'])
        user.set_password(request.POST['password'])
        if request.POST['role'] == '1':
            user.role = 1
            user.is_staff = True
            user.is_superuser = True
        user.is_active = 1
        user.save()
        if not a:
            messages.error(request, "Email is already registered ")
            return HttpResponseRedirect(reverse('register'))
        else:
            # a.update(is_active=1)
            # if request.POST['role'] == '1':
            #     a.update(role=1)

            return render(request, 'authentication/login.html')

    return render(request, 'authentication/register.html')


def user_index(request):
    if not request.user.is_authenticated:
        return redirect('index/')
    if request.user.is_staff or request.user.is_superuser:
        return


def get_users(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        return render(request, 'authentication/users.html', {'users': users})


def get_user_details(request, id):
    if request.method == 'GET':
        user = CustomUser.get_by_id(id)
        return render(request, 'authentication/user.html', {'user': user})


def update_user(request, id):
    if not request.user.is_authenticated:
        return redirect('index/')
    user = CustomUser.get_by_id(id)
    return render(request, 'authentication/update.html', {'user': user})


def delete_user(request, id):
    user = CustomUser.get_by_id(id)
    if user:
        user.delete()
        users = CustomUser.objects.all()
        return render(request, 'authentication/users.html', {'users': users})
    else:
        user = CustomUser.get_by_id(id)
        messages.error(request, 'Fails')
    return render(request, 'authentication/user.html', {'user': user})


def save_user(request, id):
    if not request.user.is_authenticated:
        return redirect('index/')
    if request.method == 'POST':
        for i in request.POST:
            if request.POST[i] == '':
                messages.error(request, f"{i} must be field")
                return redirect('update', id=id)
        print(request.POST)
        first_name = request.POST['user_name']
        last_name = request.POST['last_name']
        middle_name = request.POST['middle_name']
        password = request.POST['password']
        role = request.POST['role'] if 'role' in request.POST else None
        is_active = request.POST['is_active'] if 'is_active' in request.POST else None

        user = CustomUser.get_by_id(id)
        user.update(first_name=first_name,
                    last_name=last_name,
                    middle_name=middle_name,
                    password=password,
                    role=role,
                    is_active=is_active)
        return redirect('user', id=user.id)
    else:
        return redirect('index/')

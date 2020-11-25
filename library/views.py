from django.shortcuts import render, redirect
from .forms import CreateUserForm, CreateBookForm
from . models import Reader, Book
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'index.html', context={})


def userRegistration(request):
    if request.method == 'POST':

        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'user_reg.html', {'form': form, 'img_obj': img_obj})
    else:
        form = CreateUserForm()
    return render(request, 'user_reg.html', {'form': form})


def books(request):
    if request.method == 'POST':
        books = CreateBookForm(request.POST, request.FILES)
        if books.is_valid():
            books.save()
            img_obj = books.instance
            return render(request, 'book_regs.html', {'books': books, 'img_obj': img_obj})
    else:
        books = CreateBookForm()
    return render(request, 'book_regs.html', {'books': books,})


def allUsers(request):
    all_users = Reader.objects.all().order_by('created_at')
    context = {'users': all_users}
    return render(request, 'all_users.html', context)


def allBooks(request):
    all_books = Book.objects.all().order_by('created_at')
    context = {'books': all_books}
    return render(request, 'all_books.html', context)



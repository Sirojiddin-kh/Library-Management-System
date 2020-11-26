from django.shortcuts import render, redirect
from .forms import CreateUserForm, CreateBookForm, CreateReceivedForm
from . models import Reader, Book, Received
from django.views.generic import DetailView
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
    return render(request, 'book_regs.html', {'books': books})


def allUsers(request):
    all_users = Reader.objects.all().order_by('created_at')
    total_users = all_users.count()
    context = {'users': all_users, 'total_users': total_users}
    return render(request, 'all_users.html', context)


def allBooks(request):
    all_books = Book.objects.all().order_by('created_at')
    total_books = all_books.count()
    context = {'books': all_books, 'total_books': total_books}
    return render(request, 'all_books.html', context)


def receivedBooks(request):
    received = CreateReceivedForm()
    if request.method == 'POST':
        received = CreateReceivedForm(request.POST)
        if received.is_valid():
            received.save()
            return redirect('index')
    return render(request,  'Received_Form.html', {'received': received,})


def allorders(request):
    orders = Received.objects.all().order_by('-received_at')
    context = {'orders': orders}
    return render(request, "All_Orders.html", context)


class UserDetailView(DetailView):
    template_name = 'detail.html'
    model = Reader
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list'] = Reader.objects.all().exclude(id=self.object.id)
        return context


class BookDetailView(DetailView):
    template_name = 'detailBook.html'
    model = Book
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list'] = Book.objects.all().exclude(id=self.object.id)
        return context



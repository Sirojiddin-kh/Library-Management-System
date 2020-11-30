from django.shortcuts import render, redirect
from .forms import CreateUserForm, CreateBookForm, CreateReceivedForm
from . models import Reader, Book, Received
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm


def index(request):
    users = Reader.objects.all()
    books = Book.objects.all()
    received = Received.objects.all()
    total_receives = received.count()
    total_users = users.count()
    total_books = books.count()
    context = {'utotal':total_users, 'btotal': total_books, 'receives': total_receives}

    return render(request, 'index.html', context)


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
    all_users = Reader.objects.all().order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(all_users, 5)
    try:
        all_users = paginator.page(page)
    except PageNotAnInteger:
        all_users = paginator.page(1)
    except EmptyPage:
        all_users = paginator.page(paginator.num_pages)
    context = {'users': all_users}
    return render(request, 'all_users.html', context)


def allBooks(request):
    all_books = Book.objects.all().order_by('created_at')
    total_books = all_books.count()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_books, 5)
    try:
        all_books = paginator.page(page)
    except PageNotAnInteger:
        all_books = paginator.page(1)
    except EmptyPage:
        all_books = paginator.page(paginator.num_pages)
    context = {'books': all_books, 'total_books': total_books}
    return render(request, 'all_books.html', context)


def receivedBooks(request):
    # book = Book.objects.get(id=pk)
    received = CreateReceivedForm()
    if request.method == 'POST':
        received = CreateReceivedForm(request.POST)
        if received.is_valid():
            book = received.cleaned_data['book']
            selected_book = Book.objects.get(id=book.id)
            if selected_book.amount > 0:
                received.save()
                selected_book.amount -= 1
                if selected_book.amount == 0:
                    selected_book.status = False
                selected_book.save()
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


def accountSettings(request, pk):
    user = Reader.objects.get(id=pk)
    form = CreateUserForm(instance=user)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('allusers')
    context = {'form': form}
    return render(request, 'Account_Settings.html', context)


def bookSettings(request, pk):
    book = Book.objects.get(id=pk)
    form = CreateBookForm(instance=book)
    if request.method == "POST":
        form.save()
        return redirect('allusers')
    context = {'form': form}
    return render(request, 'Book_Settings.html', context)


def deleteUser(request, pk):
    deluser = Reader.objects.get(id=pk)
    if request.method == 'POST':
        deluser.delete()
        return redirect('allusers')
    context = {'deluser': deluser}
    return render(request, 'delete_user.html', context)


def deleteBook(request, pk):
    delbook = Book.objects.get(id=pk)
    if request.method == 'POST':
        delbook.delete()
        return redirect('allbooks')
    context = {'delbook': delbook}
    return render(request, 'delete_book.html', context)


def searchuser(request):
    search = request.GET.get('allusers')
    user_list = Reader.objects.filter(full_name__icontains=search)
    context = {'usearch': user_list}
    return render(request, 'user_search.html', context)


def searchbook(request):
    search = request.GET.get('allbooks')
    book_list = Book.objects.filter(name__icontains=search)
    context = {'bsearch': book_list}
    return render(request, 'book_search.html', context)

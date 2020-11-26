from django.urls import path
from . import views
from . views import UserDetailView, BookDetailView

urlpatterns = [
    path('', views.index, name="index"),
    path('user_reg/', views.userRegistration, name="user"),
    path('books/', views.books, name="book"),
    path('allusers/', views.allUsers, name="allusers"),
    path('all_books/', views.allBooks, name="allbooks"),
    path('receivedbook/', views.receivedBooks, name="received"),
    path('allorders/', views.allorders, name="orders"),
    path('allusers/<int:pk>', UserDetailView.as_view(), name="detailuser"),
    path('all_books/<int:pk>', BookDetailView.as_view(), name="detailbook" )
]
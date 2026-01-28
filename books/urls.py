from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<slug:slug>/edit/', views.edit_book, name='edit_book'),
    path('books/<slug:slug>/delete/', views.delete_book, name='delete_book'),
    path('books/<slug:slug>/', views.book_details, name='book_details'),
]
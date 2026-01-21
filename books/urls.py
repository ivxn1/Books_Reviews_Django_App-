from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
]
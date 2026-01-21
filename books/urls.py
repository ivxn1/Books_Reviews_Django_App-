from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<slug:slug>/', views.book_details, name='book_details'),
]
from django.urls import path

app_name = 'books'

urlpatterns = [
    path('books/', 'book_list', name='book_list'),
]
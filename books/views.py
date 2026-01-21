from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from books.models import Book


# Create your views here.

def book_list(request:HttpRequest) -> HttpResponse:
    books = Book.objects.all()

    context = {
        'page_title': 'Book List',
        'books': books,
    }

    return render(request, 'book_list.html', context)

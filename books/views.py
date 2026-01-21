from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from books.models import Book


# Create your views here.

def book_list(request:HttpRequest) -> HttpResponse:
    books = Book.objects.annotate(
        average_rating=models.Avg('reviews__rating')
    ).order_by('title')

    genres_count = books.values_list('genre', flat=True).distinct().count()
    total_reviews = sum(book.reviews.count() for book in books)
    avg_reviews = total_reviews / books.count() if books.count() > 0 else 0

    context = {
        'page_title': 'Book List',
        'books': books,
        'genres_count': genres_count,
        'total_reviews': total_reviews,
        'avg_reviews': avg_reviews,
    }

    return render(request, 'book_list.html', context)

def book_details(request:HttpRequest, slug:str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)

    context ={
        'page_title': book.title,
        'book': book,
    }

    return render(request, 'book_details.html', context)
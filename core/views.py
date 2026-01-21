from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from books.models import Book
from reviews.models import Review


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    latest_books = Book.objects.order_by('-published_date')[:3]
    latest_reviews = Review.objects.order_by('-created_at')[:3]

    context = {
        'page_title': 'Home',
        'latest_books': latest_books,
        'latest_reviews': latest_reviews,
    }

    return render(request, 'index.html', context)
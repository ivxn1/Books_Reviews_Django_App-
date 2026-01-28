from django.db import models
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify

from books.forms import BookFormBase, BookFormEdit, BookFormDelete, BookSearchForm, BookFormCreate
from books.models import Book


# Create your views here.

def book_list(request:HttpRequest) -> HttpResponse:
    books = Book.objects.annotate(
        average_rating=models.Avg('reviews__rating')
    ).order_by('title')

    form = BookSearchForm(request.GET)

    if form.is_valid():
        query = form.cleaned_data.get('query')
        books = books.filter(
            Q(title__icontains=query)
                |
            Q(author__icontains=query)
        )

    genres_count = books.values_list('genre', flat=True).distinct().count()
    total_reviews = sum(book.reviews.count() for book in books)
    avg_reviews = total_reviews / books.count() if books.count() > 0 else 0

    context = {
        'page_title': 'Book List',
        'books': books,
        'form': form,
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

def add_book(request:HttpRequest) -> HttpResponse:

    form = BookFormCreate(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        # Redirect to the book details page after saving
        return redirect('books:book_list')

    context = {
        'page_title': 'Add Book',
        'form': form,
    }

    return render(request, 'book/book_add_form.html', context)

def edit_book(request:HttpRequest, slug:str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    form = BookFormEdit(request.POST or None, instance=book)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('books:book_list')

    context = {
        'page_title': f'Edit {book.title}',
        'book': book,
        'form': form,
    }

    return render(request, 'book/book_edit_form.html', context)

def delete_book(request:HttpRequest, slug:str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    form = BookFormDelete(request.POST or None, instance=book)
    if request.method == "POST" and form.is_valid():
        book.delete()
        return redirect('books:book_list')

    context = {
        'page_title': f'Delete {book.title}',
        'book': book,
        'form': form,
    }

    return render(request, 'book/book_delete_form.html', context)

from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from books.models import Book
from reviews.models import Review
from reviews.forms import ReviewFormCreate, ReviewFormEdit, ReviewFormDelete

app_name = 'reviews'

# Create your views here.
def reviews_list(request: HttpRequest) -> HttpResponse:

    reviews = Review.objects.select_related('book').order_by('-created_at')
    total_reviewers = Review.objects.values('author').distinct().count()
    avg_rating = Review.objects.aggregate(average_rating=models.Avg('rating'))['average_rating']

    context = {
        'page_title': 'Book Reviews',
        'reviews': reviews,
        'total_reviewers': total_reviewers,
        'avg_rating': avg_rating,
    }

    return render(request, 'reviews_list.html', context)

def review_details(request: HttpRequest, review_id: int) -> HttpResponse:
    review = get_object_or_404(Review, id=review_id)

    context = {
        'page_title': f'Review by {review.author}',
        'review': review,
    }

    return render(request, 'review_details.html', context)

def add_review(request: HttpRequest) -> HttpResponse:
    form = ReviewFormCreate(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('reviews:list')

    context = {
        'page_title': 'Add Review',
        'form': form,
    }

    return render(request, 'reviews/review_add_form.html', context)

def edit_review(request: HttpRequest, review_id: int) -> HttpResponse:
    review = get_object_or_404(Review, id=review_id)
    form = ReviewFormEdit(request.POST or None, instance=review)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('reviews:list')

    context = {
        'page_title': f'Edit Review by {review.author}',
        'review': review,
        'form': form,
    }

    return render(request, 'reviews/review_edit_form.html', context)

def delete_review(request: HttpRequest, review_id: int) -> HttpResponse:
    review = get_object_or_404(Review, id=review_id)
    form = ReviewFormDelete(request.POST or None, instance=review)

    if request.method == "POST" and form.is_valid():
        review.delete()
        return redirect('reviews:list')

    context = {
        'page_title': f'Delete Review by {review.author}',
        'review': review,
        'form': form,
    }

    return render(request, 'reviews/review_delete_form.html', context)

def create_review_by_book(request:HttpRequest, slug:str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    form = ReviewFormCreate(request.POST or None, initial={'book': book})

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('books:book_details', slug=slug)

    context = {
        'page_title': f'Add Review for {book.title}',
        'book': book,
        'form': form,
    }

    return render(request, 'reviews/review_add_form.html', context)

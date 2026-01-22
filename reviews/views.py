from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from reviews.models import Review


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


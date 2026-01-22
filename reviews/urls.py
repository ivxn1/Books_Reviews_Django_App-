from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('reviews/', views.reviews_list, name='list')
]
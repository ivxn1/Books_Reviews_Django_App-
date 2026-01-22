from reviews import views

app_name = 'reviews'
from django.urls import path, include

urlpatterns = [
    path('reviews/', include([
        path('', views.reviews_list, name='list'),

    ])),
]
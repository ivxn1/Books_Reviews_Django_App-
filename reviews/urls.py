from django.urls import path, include

from reviews import views

app_name = 'reviews'
from django.urls import path, include

urlpatterns = [
    path('reviews/', include([
        path('', views.reviews_list, name='list'),
        path('<int:review_id>/', views.review_details, name='details')
        ]
    )),


]
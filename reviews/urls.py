from django.urls import path, include

from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('reviews/', include([
        path('', views.reviews_list, name='list'),
        path('add/', views.add_review, name='add_review'),
        path('<int:review_id>/edit/', views.edit_review, name='edit_review'),
        path('<int:review_id>/delete/', views.delete_review, name='delete_review'),
        path('<int:review_id>/', views.review_details, name='details'),
        ]
    )),
    path('books/<slug:slug>/reviews/create/', views.create_review_by_book, name='create_review_by_book'),

]
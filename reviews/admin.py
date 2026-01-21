from django.contrib import admin

from reviews.models import Review


# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'rating', 'created_at', 'book']
    search_fields = ['author', 'body', 'book__title']
    list_filter = ['rating', 'created_at']
    ordering = ['-created_at',]

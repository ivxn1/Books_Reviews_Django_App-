from django.contrib import admin

from books.models import Book


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre']
    search_fields = ['title', 'author', 'isbn']
    list_filter = ['genre', 'author', 'country']
    ordering = ['title',]

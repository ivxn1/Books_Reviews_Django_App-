from django.db import models

# Create your models here.

class Review(models.Model):
    author = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )

    body = models.TextField()
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    book = models.ForeignKey(
        to='books.Book',
        on_delete=models.CASCADE,
        related_name = 'reviews',
        blank=True,
        null=True
    )
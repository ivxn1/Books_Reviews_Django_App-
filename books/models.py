from django.db import models
from books.choices import GenreTextChoices

# Create your models here.

class Book(models.Model):


    title = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    isbn = models.CharField(
        max_length=12,
        unique=True,
    )

    genre = models.CharField(
        max_length=20,
        choices=GenreTextChoices
    )

    publishing_date = models.DateField(
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField()

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    author = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )

    country = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    pages = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    available = models.BooleanField(
        default=True
    )

    tag = models.ManyToManyField(
        to='Tag',
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.lower().replace(" ", "-")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Tag(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        null=False
    )

    books = models.ManyToManyField(
        to=Book,
        related_name='tags',
        blank=True,
    )

    def __str__(self):
        return self.name
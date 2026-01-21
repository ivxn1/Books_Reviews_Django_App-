from django.db import models

# Create your models here.

class Book(models.Model):

    class GenreTextChoices(models.TextChoices):
        FANTASY = "Fantasy", "Fantasy"
        HORROR = "Horror", "Horror"
        ROMANCE = "Romance", "Romance"
        THRILLER = "Thriller", "Thriller"
        SCI_FI = "Sci-Fi", "Sci-Fi"
        DOCUMENTARY = "Documentary", "Documentary"

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

    def __str__(self):
        return f"{self.title} by {self.author}"

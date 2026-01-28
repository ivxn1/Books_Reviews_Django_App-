from django.db import models

class GenreTextChoices(models.TextChoices):
    FANTASY = "Fantasy", "Fantasy"
    HORROR = "Horror", "Horror"
    ROMANCE = "Romance", "Romance"
    THRILLER = "Thriller", "Thriller"
    SCI_FI = "Sci-Fi", "Sci-Fi"
    DOCUMENTARY = "Documentary", "Documentary"
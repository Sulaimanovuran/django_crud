from django.db import models


class Genre(models.Model):
    objects = None
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='book_images')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.title

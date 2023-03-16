from django.contrib import admin

from book.models import Book, Genre

admin.site.register(Book)
admin.site.register(Genre)
from django import forms
from .models import *


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'cover', 'price', 'year', 'slug', 'genre']

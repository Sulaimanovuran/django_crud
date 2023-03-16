from django.urls import path

from .views import *

urlpatterns = [
    path('', BookList.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add/', AddBook.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('category/<int:gen_id>/', BookCategory.as_view(), name='category'),
    path('book/<slug:book_slug>/', ShowBook.as_view(), name='book'),
    path('edit/<slug:book_slug>/', BookEdit.as_view(), name='edit'),
    path('delete/<slug:book_slug>/', BookRemove.as_view(), name='delete')
]

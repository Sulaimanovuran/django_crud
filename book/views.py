from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import AddBookForm

'''
FBV - Function Based View
CBV - Class Based View
Heello John Snow

Hello Sam Smith
'''

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить продукт', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


class BookList(ListView):
    model = Book
    template_name = 'book/index.html'
    context_object_name = 'books'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Genre.objects.all()
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cats'] = cats
        return context

    def get_queryset(self):
        return Book.objects.all().order_by('-created_date')


class ShowBook(DetailView):
    model = Book
    template_name = 'book/detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'book_slug'  #slug

    # pk_url_kwarg = 'some_name'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Genre.objects.all()
        context['menu'] = menu
        context['title'] = context['post']
        context['cats'] = cats
        return context


class AddBook(CreateView):
    form_class = AddBookForm
    template_name = 'book/addbook.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Genre.objects.all()
        context['menu'] = menu
        context['title'] = "Добавление книги"
        context['cats'] = cats
        return context


class BookEdit(UpdateView):
    model = Book
    form_class = AddBookForm
    template_name = 'book/edit.html'
    slug_url_kwarg = 'book_slug'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Genre.objects.all()
        context['menu'] = menu
        context['title'] = "Редактирование книги"
        context['cats'] = cats
        return context


class BookRemove(DeleteView):
    model = Book
    template_name = 'book/delete.html'
    success_url = reverse_lazy('home')
    slug_url_kwarg = 'book_slug'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Genre.objects.all()
        context['menu'] = menu
        context['title'] = "Удаление книги"
        context['cats'] = cats
        return context


class BookCategory(ListView):
    model = Book
    template_name = 'book/index.html'
    context_object_name = 'books'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Genre.objects.all()
        context['menu'] = menu
        context['title'] = 'Категория: ' + str(context['books'][0].genre)
        context['cats'] = cats
        return context

    def get_queryset(self):
        return Book.objects.filter(genre__pk=self.kwargs['gen_id'])

def index(request):
    ns = Book.objects.all()
    cats = Genre.objects.all()
    context = {
        'title': "Главная страница",
        'menu': menu,
        'news': ns,
        'cats': cats,
        'cat_selected': 0,
    }
    return render(request, 'book/index.html', context=context)


def add_page(request):
    return HttpResponse('Test')
    # if request.method == 'POST':
    #     form = AddNewsForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    # else:
    #     form = AddNewsForm()
    # return render(request, 'news/add_page.html', {'form': form, 'title': "Опубликовать новость", 'menu': menu})


def about(request):
    return HttpResponse('Test')


def contact(request):
    return HttpResponse('Test')


def login(request):
    return HttpResponse('Test')


def cat_view(request, cat_id):
    news = Book.objects.filter(category_id=cat_id)
    cats = Genre.objects.all()
    context = {
        'title': 'Категории',
        'menu': menu,
        'news': news,
        'cats': cats,
        'cat_selected': cat_id
    }
    return render(request, 'news/index.html', context=context)

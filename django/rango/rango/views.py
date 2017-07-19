from django.shortcuts import render, get_object_or_404
from .models import Page, Category
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')


def show_category(request, category_name_slug):
    context_dict = {}
    category = get_object_or_404(Category, slug=category_name_slug)
    pages = Page.objects.filter(category=category)
    context_dict['pages'] = pages
    context_dict['category'] = category
    return render(request, 'rango/category.html', context_dict)

from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category


def store(request, category_slug=None):
    if category_slug is not None:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=selected_category, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)
    context = {
        'products': products
    }
    return render(request, 'store.html', context)



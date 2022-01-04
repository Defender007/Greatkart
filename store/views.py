from django.shortcuts import get_object_or_404, render

from .models import Product
from category.models import Category

def store(request, category_slug=None):
    category = None
    products = None
    prod = None
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=category, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render (request, 'store.html', context)

def product_detail(request, category_slug, product_slug):
    return render(request, 'product_detail.html')
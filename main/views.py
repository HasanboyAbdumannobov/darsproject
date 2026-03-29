from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-id')
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'index.html', context)


def category_products(request, id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    context = {
        'categories': categories,
        'category': category,
        'products': products,
    }
    return render(request, 'category_products.html', context)


def product_detail(request, id):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id)
    context = {
        'categories': categories,
        'product': product,
    }
    return render(request, 'product_detail.html', context)
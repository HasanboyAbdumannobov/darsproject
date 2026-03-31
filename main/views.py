from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.contrib import messages
from .cart import Cart

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

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    cart = Cart(request)

    quantity = 1
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))
        except (TypeError, ValueError):
            quantity = 1

    quantity = max(1, quantity)
    cart.add(product_id=product.id, quantity=quantity)
    messages.success(request, f'{product.name} cartga qo\'shildi.')

    next_url = request.POST.get('next_url') or request.GET.get('next')
    if next_url:
        return redirect(next_url)
    return redirect('cart_detail')



def cart_detail(request):
    categories = Category.objects.all()
    cart = Cart(request)
    cart_items = request.session.get('cart', {})
    product_ids = [int(product_id) for product_id in cart_items.keys()]
    products = Product.objects.filter(id__in=product_ids, available=True)
    products_map = {product.id: product for product in products}

    items = []
    for product_id, quantity in cart_items.items():
        product = products_map.get(int(product_id))
        if not product:
            continue
        items.append(
            {
                'product': product,
                'quantity': quantity,
                'subtotal': product.price * quantity,
            }
        )

    total_price = cart.total_price(products_map)

    return render(
        request,
        'shop/cart.html',
        {
            'categories': categories,
            'items': items,
            'total_price': total_price,
            'page_title': 'Cart',
        },
    )



def decrease_cart_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.decrease(product_id=product.id)
    messages.info(request, f'{product.name} quantity kamaytirildi.')
    return redirect('cart_detail')



def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.remove(product_id=product.id)
    messages.warning(request, f'{product.name} cartdan o\'chirildi.')
    return redirect('cart_detail')
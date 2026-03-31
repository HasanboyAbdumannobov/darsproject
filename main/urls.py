from django.urls import path
from .views import index, category_products, product_detail, add_to_cart, cart_detail, Cart
urlpatterns = [
    path('', index, name='index'),
    path('category/<int:id>/', category_products, name='category_products'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('cart/', )

]
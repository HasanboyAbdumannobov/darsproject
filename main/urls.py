from django.urls import path
from .views import index, category_products, product_detail, add_to_cart, cart_detail, Cart, remove_from_cart, decrease_cart_item
urlpatterns = [
    path('', index, name='index'),
    path('category/<int:id>/', category_products, name='category_products'),
    path('product/<int:id>/', product_detail, name='product_detail'),
        path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/decrease/<int:product_id>/', decrease_cart_item, name='decrease_cart_item'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),

]
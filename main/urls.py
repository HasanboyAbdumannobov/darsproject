from django.urls import path
from .views import index, category_products, product_detail, cart, checkout, login_view, register_view, profile

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:id>/', category_products, name='category_products'),
    path('product/<int:id>/', product_detail, name='product_detail'),


]
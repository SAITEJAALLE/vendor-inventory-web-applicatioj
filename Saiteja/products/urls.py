from django.urls import path
from .views import add_product, product_list, vendor_orders, user_orders, order_product, order_success

urlpatterns = [
    path('add_product/', add_product, name='add_product'),
    path('', product_list, name='product_list'),
    path('order/<int:product_id>/', order_product, name='order_product'),
    path('vendor_orders/', vendor_orders, name='vendor_orders'),
    path('user_orders/', user_orders, name='user_orders'),
    path('order_success/', order_success, name='order_success'),
]

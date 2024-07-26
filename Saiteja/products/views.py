from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, OrderForm
from .models import Product, Order
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html') 

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

def product_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(name__icontains=search_query)
    else:
        products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'search_query': search_query})

@login_required
def vendor_orders(request):
    if request.user.is_vendor:
        products = Product.objects.filter(vendor=request.user)
        orders = Order.objects.filter(product__in=products)
        return render(request, 'products/orders.html', {'orders': orders})
    else:
        return redirect('index')

@login_required
def user_orders(request):
    if request.user.is_user:
        orders = Order.objects.filter(user=request.user)
        return render(request, 'products/orders.html', {'orders': orders})
    else:
        return redirect('index')

@login_required
def order_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.user = request.user
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'products/order_product.html', {'form': form, 'product': product})

@login_required
def order_success(request):
    return render(request, 'products/order_success.html')

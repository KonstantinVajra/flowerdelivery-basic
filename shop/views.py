from django.shortcuts import render

from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from .forms import OrderForm

def product_list(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = UserCreationForm()

    return render(request, "shop/register.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("product_list")
    return redirect("product_list")

def create_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect("order_success")
    else:
        form = OrderForm()

    return render(request, "shop/order_form.html", {
        "form": form,
        "product": product
    })

def order_success(request):
    return render(request, "shop/order_success.html")
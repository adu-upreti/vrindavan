from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *

@login_required
def admin_dashboard(request):
    data = {
        'dashboard_active_page': 'active'
    }
    return render(request, "adminfile/dashboard.html", data)

@login_required
def Product_form(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product is saved successfully!")
            return redirect('product_form')
        else:
            messages.error(request, "There was an error saving the product.")
    else:
        form = ProductForm()

    return render(request, "adminfile/add-product.html", {"form": form})

# Update product
@login_required
def update_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_product')
    else:
        form = ProductForm(instance=product)
    return render(request, 'adminfile/update_product.html', {'form': form})


# Delete single product
@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    product.delete()
    messages.success(request, 'Product has been deleted successfully.')
    return redirect('admin_product')


# Delete selected products
@login_required
def delete_selected_products(request):
    if request.method == 'POST':
        selected_products = request.POST.getlist('selected_products')
        if selected_products:
            Products.objects.filter(id__in=selected_products).delete()
            messages.success(request, 'Selected products have been deleted successfully.')
        else:
            messages.error(request, 'No products were selected for deletion.')
    return redirect('admin_product')
   

@login_required
def add_cat(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_product')
    else:
        form = CategoryForm()
    return render(request, "adminfile/add-category.html", {'form': form})

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('admin_product')

def A_product(request):
    product_list = Products.objects.all()
    category_list = Category.objects.all()

    datas = {
        'categories': category_list,
        'products': product_list,
    }

    return render(request, "adminfile/products.html", datas)

@login_required
def Userlist(request):
    
    return render(request, "adminfile/userlist.html")


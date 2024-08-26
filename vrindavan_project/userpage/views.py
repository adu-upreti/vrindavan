from django.shortcuts import render
from adminpage.models import*


def Menu(request):
    # Replace 'Category1', 'Category2', and 'Category3' with your actual category names
    category1 = Category.objects.get(cat_name='Category1')
    category2 = Category.objects.get(cat_name='Category2')
    category3 = Category.objects.get(cat_name='Category3')

    # Fetch products for each category if needed
    products_category1 = Products.objects.filter(category=category1)
    products_category2 = Products.objects.filter(category=category2)
    products_category3 = Products.objects.filter(category=category3)

    data = {
        'category1': category1,
        'category2': category2,
        'category3': category3,
        'products_category1': products_category1,
        'products_category2': products_category2,
        'products_category3': products_category3,
    }

    return render(request, "user/menu.html", data)

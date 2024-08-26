from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *



urlpatterns = [

    path('',admin_dashboard,name="admin_dashboard"),
    path('user-list/',Userlist, name='userlist'),
    path('product/',A_product, name="admin_product"),
    path('add-product/',Product_form, name="product_form"),
    path('delete_category/<int:category_id>/',delete_category, name='delete_category'),
    path('delete_product/<int:product_id>/',delete_product, name='delete_product'),
    path('delete-selected-products/',delete_selected_products, name='delete_selected_products'),  
    path('update-product/<int:product_id>/',update_product, name='update_product'),
    path('add-category/',add_cat, name="AddCategory"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
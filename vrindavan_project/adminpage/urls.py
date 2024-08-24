from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('',views.admin_dashboard,name="admin_dashboard"),
    path('product/', views.A_product, name="admin_product"),
    path('add-product/', views.Product_form, name="product_form"),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete-selected-products/', views.delete_selected_products, name='delete_selected_products'),  
    path('update-product/<int:product_id>/', views.update_product, name='update_product'),
    path('add-category/', views.add_cat, name="AddCategory"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
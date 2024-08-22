from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [

    
    path('login/', Login,name="adminlogin"),
    path('signup/', register, name="adminregister"),\
     path('admin-dashboard/', admin_dashboard,name="admin_dashboard"),
   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
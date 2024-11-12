from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userpage.urls')),
    path('mycard/', include('digitalcard.urls')),
    path('account/', include('logsign.urls')),
    path('admin-dashboard/', include('adminpage.urls')),
    path('password_reset/', include('resetpassword.urls')),
    path('', Home, name='user_dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

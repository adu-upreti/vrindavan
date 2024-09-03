# urls.py
from django.urls import path
from .views import *
from django.views.generic import TemplateView
urlpatterns = [
    path('', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_done/', TemplateView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path('password_reset_complete/', TemplateView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
]

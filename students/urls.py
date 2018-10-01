from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('register', views.register, name='register'),
]

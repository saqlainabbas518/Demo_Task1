from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm


urlpatterns = [
    path('register/', views.register , name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html', authentication_form = LoginForm) , name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html') , name = 'logout'),


]



if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.register  , name = 'register'),
    path('profile/', user_views.profile  , name = 'profile'),
    path('Login/', auth_views.LoginView.as_view(template_name='login.html') , name = 'login'),
    path('Logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
   # path('about/', views.about  , name = 'blog-about'),
]

if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
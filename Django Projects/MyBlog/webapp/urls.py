
from django.urls import path
from . import views
from .views import createpost , updatepost , postdetail ,postdelete
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name='login.html') , name = 'login' ),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html') , name = 'logout' ),
    path('register/', views.register , name = 'register'),
    path('allposts/',views.allposts, name = 'allposts'),
    path('createpost/new',createpost.as_view(), name = 'createpost'),
    path('updatepost/<int:pk>', updatepost.as_view(), name='updatepost'),
    path('postdetail/<int:pk>', postdetail.as_view(), name='postdetail'),
    path('postdelete/<int:pk>', postdelete.as_view(), name='postdelete'),
    path('myposts/', views.myposts, name='myposts'),
    path('profile/', views.profile, name='profile'),
    # path('updateprofile/', views.UpdateProfile, name='updateprofile'),
    #path('search/', views.search, name='search '),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
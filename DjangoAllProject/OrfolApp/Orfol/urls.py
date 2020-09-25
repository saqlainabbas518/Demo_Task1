from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import  createreport , reportdetail , updatereport , deletereport , profile , reportlist
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('reportlist/', views.reportlist.as_view(), name='reportlist'),
    path('',auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/',views.register, name = 'register'),
    path('category/', views.category, name='category'),
    path('searchfilter/', views.searchfilter, name='searchfilter'),
    # path('report/', views.reports, name='report'),
    path('profile/', views.profile, name='profile'),
    # path('myreports/', views.myreports, name='myreports'),
    path('createreport/',views.createreport.as_view() , name = 'createreport'),
    path('reportdetail/<int:pk>/',views.reportdetail.as_view() , name = 'reportdetail'),
    path('updatereport/<int:pk>/', views.updatereport.as_view(), name='updatereport'),
    path('deletereport/<int:pk>/', views.deletereport.as_view(), name='deletereport'),
    # path('profile/<int:pk>/', views.profile.as_view(), name='profile'),
]


if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

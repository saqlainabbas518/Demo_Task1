from django.contrib import admin
from django.urls import path
from . import views
from  . views import newpost , reportdetail , updatereport,deletereport,reportlist
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.latestreports, name='latestreports'),
    # path('viewall/', views.viewall, name='viewall'),
    # path('candidate/',views.candidate , name = 'candidate'),
    # path('reportimages', views.reportimages , name = 'reportimages'),
    path('about/', views.about , name = 'about'),
    path('blog/', views.blog, name='blog'),
    path('newpost/',newpost.as_view(), name='newpost'),
    path('reportlist/',reportlist.as_view(), name='reportlist'),
    path('deletereport/<int:pk>',deletereport.as_view(), name='deletereport'),
    path('reportdetail/<int:pk>',reportdetail.as_view(), name='reportdetail'),
    path('updatereport/<int:pk>',updatereport.as_view(),name = 'updatereport'),

]



if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)



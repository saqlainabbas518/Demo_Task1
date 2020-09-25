from django.urls import path
from .views import PostListView ,PostDetailView ,PostCreateView ,PostUpdateView ,PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view()  , name = 'blog-home'),
    path('postdetail/<int:pk>/', PostDetailView.as_view()  , name = 'postdetail'),
    path('postupdate/<int:pk>/', PostUpdateView.as_view()  , name = 'postupdate'),
    path('postdelete/<int:pk>/', PostDeleteView.as_view()  , name = 'postdelete'),
    path('postcreate/new', PostCreateView.as_view()  , name = 'postcreate'),
    path('about/', views.about  , name = 'blog-about'),
]
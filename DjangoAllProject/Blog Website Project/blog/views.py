from django.shortcuts import render,redirect
from .models import Post
from django.views.generic import ListView ,DetailView , CreateView ,DeleteView ,UpdateView


def home(requset):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(requset , 'home.html' , context ,{'title':'Home'})

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    #this is use to view all the data in html template like home.html
    # if you don't use this data will not show on the template

class PostDetailView(DetailView):
    model = Post
    template_name = 'postdetail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title' , 'content']
    template_name = 'postcreate.html'


    def form_valid(self, form): #this mehtod will work to post data will get the current logged in user id will come to know about user
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title' , 'content']
    template_name = 'postupdate.html'

    def form_valid(self, form): #this mehtod will work to post data will get the current logged in user id will come to know about user
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'post_confirm_delete.html'



def about(request):
    return render(request , 'about.html' , {'title': 'About'})


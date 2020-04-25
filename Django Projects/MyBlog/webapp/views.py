from django.shortcuts import render , redirect
from .forms import UserRegisterationForm  , newpost , UserUpdateForm , UpdateProfile
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView ,UpdateView ,DeleteView , DetailView , ListView
from django.db.models import query


@login_required
def allposts(request):
    posts = Post.objects.all()
    posts = {
        'posts':posts
    }
    return render(request , 'index.html' , posts)


@login_required
def profile(request):
     return render(request , "profile.html")


@login_required
def myposts(request):
    current_user = request.user.username
    userposts = Post.objects.filter(username__username=current_user)
    return render(request, 'viewallmyposts.html' , {'userposts':userposts})

class createpost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title' , 'content']
    template_name = 'newpost.html'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class updatepost(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title' , 'content']
    template_name = 'updatepost.html'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        return False

class postdetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'postdetail.html'


class postdelete(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Post
    template_name = 'postdelete.html'
    success_url = reverse_lazy('allposts')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        return False





def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created Successfully for {username}')
            redirect('login')
    else:
        form = UserRegisterationForm()
    return render(request , 'register.html' , {'form':form})


# @login_required
# def updateprofile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile.image)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = UpdateProfile(instance=request.user.profile.image)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'updateprofile.html')

# def search(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         allposts = Post.objects.filter(title__icontains= posts)
#         params = {'allposts' : allposts}
#     return render(request , 'search.html' , params)
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView , DetailView , CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from .forms import UserRegisterForm
from django.forms import modelformset_factory
from django.urls import reverse_lazy




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form= UserRegisterForm()
    return render(request , 'user/register.html', {'form':form})
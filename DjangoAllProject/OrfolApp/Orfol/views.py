from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from .models import Category ,Subcategory , Report ,Profile
from django.views.generic import ListView ,DeleteView , CreateView, UpdateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.decorators import login_required

@login_required
def category(request):
   all =Category.objects.all()
   context = {'all':all}
   return render(request , 'category.html' , context)


@login_required
def reports(request):
    context = {'report':Report.objects.all()}
    return render(request , 'home.html',context)

# @method_decorator(login_required, name='dispatch')
class reportlist(LoginRequiredMixin, ListView):
    model = Report
    context_object_name = 'report'
    template_name = 'home.html'

@login_required
def myreports(request):
    current_user = request.user.username
    allreports = Report.objects.filter(username__username = current_user)
    return render(request , 'profile.html' , {'allreports':allreports})


def is_valid_queryparam(param):
    return param !='' and param is not None

@login_required
def searchfilter(request):
    qs = Report.objects.all()
    cats = Category.objects.all()
    subcats= Subcategory.objects.all()
    title_contains_query = request.GET.get('title_contains')
    title_exact_query = request.GET.get('title_exact')
    title_or_author_query = request.GET.get('title_or_author')
    categories = request.GET.get('categories')
    subcategories = request.GET.get('subcategories')
    if title_contains_query !='' and title_contains_query is not None:
        qs =qs.filter(title__icontains = title_contains_query)
    else:
        messages.error(request, f'Not Found {title_contains_query}')
    if is_valid_queryparam(categories)and categories != 'Choose':
        qs = qs.filter(categories__categories=categories)
    if is_valid_queryparam(subcategories)and subcategories != 'Choose':
        qs = qs.filter(subcategories__subcategories=subcategories)
    # if title_exact_query != '' and title_exact_query is not None:
    #     qs= qs.filter(id__exact = title_exact_query)

    context = {'queryset':qs,
               'cats' : cats,
               'subcats':subcats
               }
    return render(request , 'search.html' , context)


@login_required
def profile(request):
    prof = Profile.objects.all()
    prof = {'prof':prof}
    return render(request, 'profile.html', prof)




class createreport(LoginRequiredMixin ,  CreateView):
    model = Report
    fields = ['title','categories','subcategories','city','subcity','reward','time','description']
    template_name = 'createreport.html'
    success_url = reverse_lazy('home')


class reportdetail(LoginRequiredMixin , DetailView):
    model = Report
    template_name = 'reportdetail.html'

class updatereport(LoginRequiredMixin ,  UpdateView):
    model = Report
    fields = ['title','categories','subcategories','city','subcity','image','reward','time','description']
    template_name = 'updatereport.html'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class deletereport(LoginRequiredMixin , UserPassesTestMixin, DeleteView):
    model = Report
    template_name = 'deletereport.html'
    success_url = reverse_lazy('report')


def register(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created Successfully for {username}')
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request , 'register.html' , context)





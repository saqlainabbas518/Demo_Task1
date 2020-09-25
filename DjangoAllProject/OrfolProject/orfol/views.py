from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView , DetailView , CreateView,UpdateView,DeleteView
from .models import Report , ReportImage,User , SubCategory,Category,SavedReport,Notification,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.forms import modelformset_factory
from .forms import ImageForm , createpost
from django.urls import reverse_lazy



def about(request):
    return render(request , 'orfol/about.html')

def blog(request):
    return render(request , 'orfol/blog.html')


def latestreports(request):
    obj = Report.objects.all().order_by('-date_created')[:5]
    return render(request, 'orfol/index.html', {'obj': obj})

# def viewall(request):
#     rep = Report.objects.all()
#     return render(request , 'orfol/candidates.html',{'rep':rep})


class reportlist(ListView):
    model = Report
    template_name = 'orfol/candidates.html'
    context_object_name = 'reports'
    paginate_by = 6


class newpost(LoginRequiredMixin, CreateView):
    model = Report
    form_class = createpost
    template_name = "orfol/newpost.html"
    # def get_form(self, form_class=None):
    #     if form_class is None:
    #         form_class = self.get_form(createpost)
    #     form = super(newpost, self).get_form(createpost)
    #     # current_user = self.request.user.username
    #     # form.fields['user_id'] = newpost(initial= 'current_user')
    #     # form.fields['title'].widget.attrs = {'placeholder': 'Enter Title'}
    #     # form.fields['type'].widget.attrs = {'placeholder': 'Enter type'}
    #     # form.fields['reward'].widget.attrs = {'placeholder': 'Enter reward'}
    #     # form.fields['location'].widget.attrs = {'placeholder': 'Enter location'}
    #     # form.fields['status'].widget.attrs = {'placeholder': 'Enter status active/inactive'}
    #     # form.fields['description'].widget.attrs = {'placeholder': 'Enter Description of report'}
    #     return form
    # def form_valid(self, form):
    #     form.instance.user_id == self.request.user
    #     return super().form_valid(form)



class reportdetail(DetailView):
    model = Report
    context_object_name = 'Report'
    template_name = 'orfol/reportdetail.html'


class updatereport(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Report
    fields = '__all__'
    template_name = 'orfol/updatereport.html'

    def form_valid(self, form):
        form.instance.user_id == self.request.user
        return super().form_valid(form)

    def test_func(self):
        report = self.get_object()
        if self.request.user == report.user_id:
            return True
        return False

class deletereport(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Report
    success_url = reverse_lazy('viewall')
    template_name = 'orfol/confrimdelete.html'

    def test_func(self):
        rep = self.get_object()
        if self.request.user == rep.user_id:
            return True
        return False

# @login_required
# def reportimages(request):
#     ImageFormSet = modelformset_factory(reportimages,form=ImageForm, extra=3)
#     if request.method == 'POST':
#         postform = ImageForm(request.POST , request.FILES)
#         if ImageForm.is_valid():
#             ImageForm.save()
#             return redirect('reportdetail')
#     else:
#         postform = ImageForm()
#     return  render(request , 'orfol/reportdetail.html' , {'postform':postform})






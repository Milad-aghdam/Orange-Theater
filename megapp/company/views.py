from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.views.generic import ListView, UpdateView
from company.forms import FoodhouseCraeteForm
from .models import Foodhouse



class FoodhouseView(LoginRequiredMixin, ListView):
    model = Foodhouse
    template_name = 'company/foodhouse/index.html'
    paginate_by = 20
    context_object_name = 'foodhouses'

class FoodhouseUpdateView(LoginRequiredMixin, UpdateView):
    model = Foodhouse
    template_name = 'company/foodhouse/update.html'
    form_class = FoodhouseCraeteForm
    context_object_name = 'foodhouses'



class FoodhouseCreateView(LoginRequiredMixin, View):
    template_name = 'company/foodhouse/create.html'
    form_class = FoodhouseCraeteForm
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})





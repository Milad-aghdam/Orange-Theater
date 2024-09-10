from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView
from company.forms import FoodhouseCraeteForm, FoodhubCraeteForm
from .models import Foodhouse, Foodhub
from django.urls import reverse_lazy





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

class FoodhouseDeleteView(LoginRequiredMixin, DeleteView):
    model = Foodhouse
    template_name = 'company/foodhouse/delete.html'
    success_url = reverse_lazy('company:foodhouse-list')

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


class FoodhubView(LoginRequiredMixin, ListView):
    model = Foodhub
    template_name = 'company/foodhub/index.html'
    paginate_by = 20
    context_object_name = 'foodhub'

class FoodhubUpdateView(LoginRequiredMixin, UpdateView):
    model = Foodhub
    template_name = 'company/foodhub/update.html'
    form_class = FoodhubCraeteForm
    context_object_name = 'foodhub'

class FoodhubDeleteView(LoginRequiredMixin, DeleteView):
    model = Foodhub
    template_name = 'company/foodhouse/delete.html'
    success_url = reverse_lazy('company:foodhouse-list')

class FoodhubCreateView(LoginRequiredMixin, View):
    template_name = 'company/foodhouse/create.html'
    form_class = FoodhubCraeteForm
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})

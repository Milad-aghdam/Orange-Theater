from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView
from company.forms import FoodhouseCraeteForm, FoodhubCraeteForm, UberEatsCraeteForm, JusteatCraeteForm
from .models import Foodhouse, Foodhub, UberEats, Justeat, WhatTheFork
from django.urls import reverse_lazy
from .mixin import SuperUserAccessMixin
from accounts.models import User
from accounts.forms import ProfileForm





class UserProfileView(SuperUserAccessMixin, ListView):
    model = User
    template_name = 'company/profile.html'
    context_object_name = 'users'
    
class UserUpdateView(SuperUserAccessMixin, UpdateView):
    model = User
    template_name = 'company/profile_update.html'
    form_class = ProfileForm
    context_object_name = 'user'
    success_url = reverse_lazy('company:profile-all')





class FoodhouseView(SuperUserAccessMixin, ListView):
    model = Foodhouse
    template_name = 'company/foodhouse/index.html'
    paginate_by = 20
    context_object_name = 'foodhouses'

class FoodhouseUpdateView(SuperUserAccessMixin, UpdateView):
    model = Foodhouse
    template_name = 'company/foodhouse/update.html'
    form_class = FoodhouseCraeteForm
    context_object_name = 'foodhouses'

class FoodhouseDeleteView(SuperUserAccessMixin, DeleteView):
    model = Foodhouse
    template_name = 'company/foodhouse/delete.html'
    success_url = reverse_lazy('company:foodhouse-list')

class FoodhouseCreateView(SuperUserAccessMixin, View):
    template_name = 'company/foodhouse/create.html'
    form_class = FoodhouseCraeteForm
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})




class FoodhubView(SuperUserAccessMixin, ListView):
    model = Foodhub
    template_name = 'company/foodhub/index.html'
    paginate_by = 20
    context_object_name = 'foodhub'

class FoodhubUpdateView(SuperUserAccessMixin, UpdateView):
    model = Foodhub
    template_name = 'company/foodhub/update.html'
    form_class = FoodhubCraeteForm
    context_object_name = 'foodhub'

class FoodhubDeleteView(SuperUserAccessMixin, DeleteView):
    model = Foodhub
    template_name = 'company/foodhouse/delete.html'
    success_url = reverse_lazy('company:foodhouse-list')

class FoodhubCreateView(SuperUserAccessMixin, View):
    template_name = 'company/foodhouse/create.html'
    form_class = FoodhubCraeteForm
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})




class UberEatsView(SuperUserAccessMixin, ListView):
    model = UberEats
    template_name = 'company/ubereats/index.html'
    paginate_by = 20
    context_object_name = 'ubereats'

class UberEatsUpdateView(SuperUserAccessMixin, UpdateView):
    model = UberEats
    template_name = 'company/ubereats/update.html'
    form_class = UberEatsCraeteForm
    context_object_name = 'ubereats'

class UberEatsDeleteView(SuperUserAccessMixin, DeleteView):
    model = UberEats
    template_name = 'company/ubereats/delete.html'
    success_url = reverse_lazy('company:ubereats-list')

class UberEatsCreateView(SuperUserAccessMixin, View):
    template_name = 'company/ubereats/create.html'
    form_class = UberEatsCraeteForm
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})





class JusteatView(SuperUserAccessMixin, ListView):
    model = Justeat
    template_name = 'company/justeat/index.html'
    paginate_by = 20
    context_object_name = 'justeat'

class JusteatUpdateView(SuperUserAccessMixin, UpdateView):
    model = Justeat
    template_name = 'company/justeat/update.html'
    form_class = JusteatCraeteForm
    context_object_name = 'ubereats'

class JusteatDeleteView(SuperUserAccessMixin, DeleteView):
    model = Justeat
    template_name = 'company/ubereats/delete.html'
    success_url = reverse_lazy('company:justeat-list')

class JusteatCreateView(SuperUserAccessMixin, View):
    template_name = 'company/justeat/create.html'
    form_class = JusteatCraeteForm
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})
    
    
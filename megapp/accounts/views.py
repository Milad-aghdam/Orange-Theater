from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.views import View
from .forms import UserLoginForm


class LoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/user_login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
        return render(request, self.template_name, {'form': form})
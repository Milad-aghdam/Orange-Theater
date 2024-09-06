from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class HomeView(View):
    template_name = 'interactive_bar.html'
    def get(self, request):
        return render(request, self.template_name)



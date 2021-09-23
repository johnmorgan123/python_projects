from django.shortcuts import render
from django.views import generic
# Create your views here.

class HomeView(generic.DetailView):
    template_name = 'home.html'




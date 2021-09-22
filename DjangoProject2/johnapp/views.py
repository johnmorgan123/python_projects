from django.shortcuts import render
from .models import Person
from django.views import generic


# Create your views here.

class PersonView(generic.DetailView):
    model = Person
    template_name = 'people.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'

class PersonList(generic.ListView):
    model = Person
    template_name = 'index.html'

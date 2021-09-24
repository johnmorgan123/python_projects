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


from django.http import HttpResponse
from django.template import loader


def my_about_view(request):
    # View code here...
    t = loader.get_template('about.html')
    c = {}
    return HttpResponse(t.render(c, request), content_type='application/xhtml+xml')

def my_greet_view(request):
    # View code here...
    t = loader.get_template('greet.html')
    c = {}
    return HttpResponse(t.render(c, request), content_type='application/xhtml+xml')
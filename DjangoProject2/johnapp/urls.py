from . import views
from django.urls import path
from django.shortcuts import render


urlpatterns = [
    path('about/', views.my_about_view),
    path('greet/', views.my_greet_view),
    path('people/<slug:slug>/', views.PersonView.as_view(), name='person_view'),
    path('', views.PersonList.as_view(), name='home')

]

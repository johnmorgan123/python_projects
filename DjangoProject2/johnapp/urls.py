from . import views
from django.urls import path

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('people/<slug:slug>/', views.PersonView.as_view(), name='person_view'),
    path('', views.PersonList.as_view(), name='home')

]

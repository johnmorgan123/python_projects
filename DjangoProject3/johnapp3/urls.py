from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home_view')

]

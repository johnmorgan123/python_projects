from django.db import models

# Create your models here.

class Home(models.Model):

    def __str__(self):
        return 'home.html'



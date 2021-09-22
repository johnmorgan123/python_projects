from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateTimeField()
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
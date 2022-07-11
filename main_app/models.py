from django.db import models
from django.urls import reverse

# Create your models here.
class ActionFigure(models.Model):
    name = models.CharField(max_length=100)
    originmovie = models.CharField(max_length=100)
    ability = models.CharField(max_length=250)
    price = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'actionfigure_id': self.id})

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title} on {self.year}"

    class Meta: 
        ordering = ['year']

    actionfigure = models.ForeignKey(ActionFigure, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} on {self.year}"
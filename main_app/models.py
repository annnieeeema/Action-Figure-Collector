from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Superpower(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.name}'

  def get_absolute_url(self):
    return reverse('superpowers_detail', kwargs={'pk': self.id})


class ActionFigure(models.Model):
    name = models.CharField(max_length=100)
    originmovie = models.CharField(max_length=100)
    ability = models.CharField(max_length=250)
    price = models.CharField(max_length=10)
    # Add the M:M relationship
    superpowers = models.ManyToManyField(Superpower)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
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
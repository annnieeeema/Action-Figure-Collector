from django.db import models

# Create your models here.
class ActionFigure(models.Model):
    name = models.CharField(max_length=100)
    originmovie = models.CharField(max_length=100)
    ability = models.CharField(max_length=250)
    price = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
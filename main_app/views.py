from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# define home view
def home(request):
    return HttpResponse('<h1>Hello! Welcome to the superhero league!</h1>')
def about(request):
    return render(request, 'about.html')
def actionfigures_index(request):
    return render(request, 'actionfigures/index.html', {'actionfigures': actionfigures})

class ActionFigure:
    def __init__(self, name, movie, ability, price ):
        self.name = name
        self.movie = movie
        self.ability = ability
        self.price = price

actionfigure = [
    ActionFigure('', '', '', ''), 
    ActionFigure('', '', '', ''), 
    ActionFigure('', '', '', ''), 
    ActionFigure('', '', '', ''), 
]
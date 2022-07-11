from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ActionFigure
from .forms import MovieForm

# Create your views here.
# define home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def actionfigures_index(request):
    return render(request, 'actionfigures/index.html', {'actionfigures': actionfigures})

def actionfigures_index(request):
    actionfigures = ActionFigure.objects.all()
    return render(request, 'actionfigures/index.html', { 'actionfigures': actionfigures })

def actionfigures_detail(request, actionfigure_id):
    actionfigure = ActionFigure.objects.get(id=actionfigure_id)
    movie_form = MovieForm()
    return render(request, 'actionfigures/detail.html', { 'actionfigure': actionfigure, 'movie_form' : movie_form })

def add_movie(request, actionfigure_id):
    form = MovieForm(request.POST)
    if form.is_valid():
        new_movie = form.save(commit=False)
        new_movie.actionfigure_id = actionfigure_id
        new_movie.save()
    return redirect('detail', actionfigure_id=actionfigure_id)

class ActionFigureCreate(CreateView):
    model = ActionFigure
    fields = '__all__'
    success_url = '/actionfigures/'

class ActionFigureUpdate(UpdateView):
    model = ActionFigure
    fields = ['originmovie', 'ability', 'price']

class ActionFigureDelete(DeleteView):
    model = ActionFigure
    success_url = '/actionfigures/'


def superpowers_index(request):
    return render(request, 'superpowers/index.html', { 'superpowers' : superpowers })


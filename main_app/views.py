from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ActionFigure, Superpower
from .forms import MovieForm
from django.views.generic import ListView, DetailView
# from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# define home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def actionfigures_index(request):
    actionfigures = ActionFigure.objects.filter(user=request.user)
    return render(request, 'actionfigures/index.html', { 'actionfigures': actionfigures })

@login_required
def actionfigures_detail(request, actionfigure_id):
    actionfigure = ActionFigure.objects.get(id=actionfigure_id)
    superpowers_actionfigure_doesnt_have = Superpower.objects.exclude(id__in = actionfigure.superpowers.all().values_list('id'))
    movie_form = MovieForm()
    return render(request, 'actionfigures/detail.html', { 'actionfigure': actionfigure, 'movie_form' : movie_form, 'superpowers':superpowers_actionfigure_doesnt_have})

@login_required
def add_movie(request, actionfigure_id):
    form = MovieForm(request.POST)
    if form.is_valid():
        new_movie = form.save(commit=False)
        new_movie.actionfigure_id = actionfigure_id
        new_movie.save()
    return redirect('detail', actionfigure_id=actionfigure_id)

@login_required
def assoc_superpower(request, actionfigure_id, superpower_id):
    ActionFigure.objects.get(id=actionfigure_id).superpowers.add(superpower_id)
    return redirect('detail', actionfigure_id=actionfigure_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ActionFigureCreate(LoginRequiredMixin, CreateView):
    model = ActionFigure
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = '/actionfigures/'

class ActionFigureUpdate(LoginRequiredMixin, UpdateView):
    model = ActionFigure
    fields = ['originmovie', 'ability', 'price']

class ActionFigureDelete(LoginRequiredMixin, DeleteView):
    model = ActionFigure
    success_url = '/actionfigures/'

class SuperpowerList(LoginRequiredMixin, ListView):
  model = Superpower
  template_name = 'superpowers/index.html'

class SuperpowerDetail(LoginRequiredMixin, DetailView):
  model = Superpower
  template_name = 'superpowers/detail.html'

class SuperpowerCreate(LoginRequiredMixin, CreateView):
    model = Superpower
    fields = ['name']


class SuperpowerUpdate(LoginRequiredMixin, UpdateView):
    model = Superpower
    fields = ['name']


class SuperpowerDelete(LoginRequiredMixin, DeleteView):
    model = Superpower
    success_url = '/superpowers/'

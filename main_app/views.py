from django.shortcuts import render
from .models import ActionFigure

# Create your views here.
# define home view
def home(request):
    return HttpResponse('<h1>Hello! Welcome to the superhero league!</h1>')

def about(request):
    return render(request, 'about.html')

def actionfigures_index(request):
    return render(request, 'actionfigures/index.html', {'actionfigures': actionfigures})

def actionfigures_index(request):
    actionfigures = ActionFigure.objects.all()
    return render(request, 'actionfigures/index.html', { 'actionfigures': actionfigures })

def actionfigures_detail(request, actionfigure_id):
    actionfigure = ActionFigure.objects.get(id=actionfigure_id)
    return render(request, 'actionfigures/detail.html', { 'actionfigure': actionfigure })
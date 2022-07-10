from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'), 
path('about/', views.about, name='about'),
path('actionfigures/', views.actionfigures_index, name='index'), 
path('actionfigures/<int:actionfigure_id>/', views.actionfigures_detail, name='detail'),
]
from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'), 
path('about/', views.about, name='about'),
path('actionfigures/', views.actionfigures_index, name='index'), 
path('actionfigures/<int:actionfigure_id>/', views.actionfigures_detail, name='detail'),
path('actionfigures/create/', views.ActionFigureCreate.as_view(), name='actionfigures_create'),
path('actionfigures/<int:pk>/update/', views.ActionFigureUpdate.as_view(), name='actionfigures_update'),
path('actionfigures/<int:pk>/delete/', views.ActionFigureDelete.as_view(), name='actionfigures_delete'),
path('actionfigures/<int:actionfigure_id>/add_movie/', views.add_movie, name='add_movie')


]
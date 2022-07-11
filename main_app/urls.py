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
path('actionfigures/<int:actionfigure_id>/add_movie/', views.add_movie, name='add_movie'),
path('actionfigures/<int:actionfigure_id>/assoc_superpower/<int:superpower_id>/', views.assoc_superpower, name='assoc_superpower'),
path('superpowers/', views.SuperpowerList.as_view(), name='superpowers_index'),
path('superpowers/<int:pk>/', views.SuperpowerDetail.as_view(), name='superpowers_detail'),
path('superpowers/create/', views.SuperpowerCreate.as_view(), name='superpowers_create'),
path('superpowers/<int:pk>/update/', views.SuperpowerUpdate.as_view(), name='superpowers_update'),
path('superpowers/<int:pk>/delete/', views.SuperpowerDelete.as_view(), name='superpowers_delete'),
path('accounts/signup/', views.signup, name='signup'),
]
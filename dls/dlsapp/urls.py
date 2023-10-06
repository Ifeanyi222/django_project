from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('dlsapp/', views.dlsapp, name='dlsapp'),
    path('dlsapp/details/<int:id>', views.details, name='details')
]
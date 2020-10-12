from django.urls import path
from .import views

urlpatterns =[
  path('', views.home, name='home')
  # add path for Gallery View
  
]
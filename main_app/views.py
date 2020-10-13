from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
# import boto3
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Video


# Create your views here.
def home(request):
  return render(request, 'home.html')

def gallery(request):
  return render(request, 'gallery.html')


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
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


  # # videos views

  # # get private videos
  # def videos_index(request):
  #   videos = Video.objects.filter(user=request.user)
  #   return render(request, 'videos/private_index.html', {'videos' : videos})
  
  # # get public videos
  # @login_required
  # def videos_index(request):
  #   videos = Video.objects.filter(user=request.user)
  #   return render(request, 'videos/videos_index.html', {'videos' : videos})

  # # create video after user submits in p5.js
  # class VideoCreate(LoginRequiredMixin, CreateView):
  #   model = Video
  #   # fields = [] , what fields?

  # class VideoUpdate(LoginRequiredMixin, UpdateView):
  #   model = Video
  #   # fields = [] , what fields!?

  # class VideoDelete(LoginRequiredMixin, DeleteView):
  #   model = Video
  #   # success_url = '/' , to private video!

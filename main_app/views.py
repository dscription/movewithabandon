from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Video
import json

# Create your views here.
def home(request):
  return render(request, 'home.html')

def gallery(request):
  return render(request, 'gallery.html')

def private_gallery(request):
  return render(request, 'private_gallery.html')


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

# @login_required
def private_index(request):
  print('private index hit')
  videos = Video.objects.filter(user=request.user)
  return render(request, 'videos/private_index.html', {'videos' : videos})


def videos_index(request):
  print('public index hit')
  videos = Video.objects.all()
  return render(request, 'videos/videos_index.html', {'videos' : videos})


def videos_create(request):
  form_data = json.loads(request.body)
  url = form_data['url']
  video = Video.objects.create(url=url,user=request.user)
  video.save()
  return render(request, 'videos/private_index.html')

def videos_delete(request,pk):
  print('----------------------------delete hit!')
  print(pk)
  # delete video by video id
  # redirect back to private gallery
  return

def videos_update(request,pk):
  video = Video.objects.filter(id = pk)
  print(video)
  video.isPrivate = not video.isPrivate
  print('-----got a video to update------', video)
  # get video by id
  # toggle ifPrivate
  return
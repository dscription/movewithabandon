from django.urls import path
from .import views

urlpatterns =[
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  # videos views
  # path('videos/', views.videos_index, name='index'),
  path('videos/private_index/', views.private_index, name='private_index'),
  path('videos/create/', views.videos_create, name='videos_create'),
  path('videos/<int:pk>/update', views.videos_update,name='videos_update'),
  path('videos/<int:pk>/delete', views.videos_delete,name='videos_delete'),
  path('experience/drawing', views.drawing, name='drawing'),
  path('experience/touch', views.touch, name='touch'),
  path('experience/control', views.control, name='control')   
  
]
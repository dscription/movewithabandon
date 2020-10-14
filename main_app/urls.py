from django.urls import path
from .import views

urlpatterns =[
  path('', views.home, name='home'),
  # path('gallery', views.gallery, name='gallery'),
  path('private_index/', views.private_index, name='private_index'),
  path('accounts/signup/', views.signup, name='signup'),
  # videos views
  path('videos/', views.videos_index, name='index'),
  path('videos/create/', views.videos_create, name='videos_create'),
  # path('videos/<int:pk>/update', views.VideoUpdate.as_view(),name='videos_update'),
  # path('videos/<int:pk>/update', views.VideoDelete.as_view(),name='videos_delete'),
]
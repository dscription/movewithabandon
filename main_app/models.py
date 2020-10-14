from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
  url = models.CharField(max_length=200)
  isPrivate = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  dateCreated = models.DateField(default=date.today)

  def __str__(self):
    return f"Video for user_id: {self.user_id} @{self.url} private: {self.isPrivate}"

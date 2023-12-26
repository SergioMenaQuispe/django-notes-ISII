from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)

  is_public = models.BooleanField(default=False)

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  username = models.CharField(max_length=30)
  password1 = models.CharField(max_length=30)
  password2 = models.CharField(max_length=30)

from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD
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

=======
# Create your models here.
>>>>>>> rama-Christian


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    # Modificacion para que una tarea sea publica
    public = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.user.username

# Creacion del modelo para los comentarios


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text}"

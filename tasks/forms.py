from django.forms import ModelForm
from .models import Task
from django import forms

from comments.models import Comment

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
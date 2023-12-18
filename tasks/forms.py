from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.title(attrs={'class': 'form-control'}),
            'description': forms.description(attrs={'class': 'form-control'}),
            'important': forms.important(attrs={'class': 'form-control'}),
        }
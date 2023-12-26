from django.forms import ModelForm
from .models import Task
from django import forms

from comments.models import Comment

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']

class RegisterForm(ModelForm):
    class Meta:
        model = Task
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario...'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña...'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña...'}),
        }
        labels = {
            'username': 'Nombre de usuario:',
            'password1': 'Ingrese contraseña:',
            'password2': 'Ingrese nuevamente la contraseña:',
        }
        
        fields = ['title', 'description', 'important', 'public']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
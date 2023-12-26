from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Task
from .models import Comment

<<<<<<< HEAD
from .forms import TaskForm
from .forms import RegisterForm
=======
from .forms import TaskForm, CommentForm
>>>>>>> rama-Christian

# Constante para signup
SIGNUP_TEMPLATE = 'signup.html'

<<<<<<< HEAD
=======

def signup(request):
    ruta='signup.html'
    if request.method == 'GET':
<<<<<<< HEAD
        return render(request, ruta, {"form": RegisterForm})
=======
        return render(request, SIGNUP_TEMPLATE, {"form": UserCreationForm})
>>>>>>> rama-Saul
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
<<<<<<< HEAD
                return render(request, ruta, {"form": RegisterForm, "error": "El usuario ya esta registrado."})

        return render(request, ruta, {"form": RegisterForm, "error": "Las contraseñas no coinciden."})
=======
                return render(request, SIGNUP_TEMPLATE, {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, SIGNUP_TEMPLATE, {"form": UserCreationForm, "error": "Passwords did not match."})
>>>>>>> rama-Saul

# prueba


>>>>>>> rama-Bruno
@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    tasks_completed = Task.objects.filter(user=request.user, datecompleted__isnull=False)

    count_completed = tasks_completed.count()
    count_not_completed = tasks.count()

    return render(request, 'tasks.html', {"tasks": tasks, "count_total": count_completed + count_not_completed, "count_completed": count_completed})



@login_required
def tasks_completed(request):
<<<<<<< HEAD
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    
    tasks_not_completed = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    count_not_completed = tasks_not_completed.count()
    count_completed = tasks.count()
    
    return render(request, 'tasks.html', {"tasks": tasks, "count_total": count_completed + count_not_completed, "count_completed": count_completed})
=======
    tasks = Task.objects.filter(
        user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {"tasks": tasks})
>>>>>>> rama-Christian


@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {"form": TaskForm, "error": "Error creating task."})
    
@login_required
def public_tasks(request):
    tasks = Task.objects.filter(is_public=True)
    return render(request, 'public_tasks.html', {'tasks': tasks})


def home(request):
    return render(request, 'home.html')

<<<<<<< HEAD
=======

@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('tasks')


>>>>>>> rama-Christian
@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task.'})


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
<<<<<<< HEAD
=======


@login_required
def task_public(request):
    tasks = Task.objects.filter(public=True)
    tasks = tasks.exclude(user=request.user)

    comments_dict = {}

    for task in tasks:
        comments = Comment.objects.filter(task=task)
        comments_dict[task.id] = comments

    print("Comentarios:", comments_dict, "\n")
    print("Tareas publicas: ", tasks, "\n")
    return render(request, 'tasks.html', {"tasks": tasks, "is_public": True, "comments_dict": comments_dict, "comment_form": CommentForm})


@login_required
def add_comment(request, task_id):
    print(f"task_id: {task_id}")
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.task = task
            new_comment.user = request.user
            new_comment.save()
            print("Comment saved successfully")
        else:
            print("Comment not saved")
    return redirect('task_public')
>>>>>>> rama-Christian

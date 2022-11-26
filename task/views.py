from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm, PerfilForm
from .models import TaskModel, PerfilModel


# Home
def home(request):
    return render(request, 'home.html')


def perfiles(request):
    return render(request, 'perfiles_tesis.html')


def temas(request):
    return render(request, 'temas_tesis.html')


def tribunales(request):
    return render(request, 'tribunales_tesis.html')


def sennalamiento(request):
    return render(request, 'sennalamiento.html')


# Visualizar de tarea
@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(TaskModel, pk=task_id)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {
            'task': task,
            'form': form
        })
    else:
        try:
            task = get_object_or_404(TaskModel, pk=task_id)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('task')
        except ValueError:
            return render(request, 'task_detail.html', {
                'task': task,
                'form': form,
                'error': "Error al actualizar"
            })


#  Eliminar tarea
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(TaskModel, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task')


# Listar tareas
@login_required
def task(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task.html', {
        'tasks': tasks
    })


# creadno una tarea
@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:

        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('task')
        except:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'error': 'Please provider valide data'
            })


def create_perfil(request):
    if request.method == 'GET':
        return render(request, 'create_perfil.html', {
            'form': PerfilForm
        })
    else:
        try:
            form = PerfilForm(request.POST)
            new_perfil = form.save(commit=False)
            new_perfil.user = request.user
            new_perfil.save()
            return redirect('perfiles')
        except:
            return render(request, 'create_perfil.html', {
                'form': PerfilForm,
                'error': 'Please provider valide data'
            })


# Creando Usuario
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # registrar usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('signin')

            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Pass no coincide'
        })


# Iniciando sesion
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'User or pass is incorrect'
            })
        else:
            login(request, user),
            return redirect('task')


# Cerrando sesion
@login_required
def signout(request):
    logout(request)
    return redirect('home')

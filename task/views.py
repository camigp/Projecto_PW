from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PerfilForm
from .models import PerfilTesisModel


def login(request):
    return render(request, 'login.html')



# Home
def home(request):
    return render(request, 'home.html')





def temas(request):
    return render(request, 'temas_tesis.html')


def tribunales(request):
    return render(request, 'tribunales_tesis.html')


def sennalamiento(request):
    return render(request, 'sennalamiento.html')








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
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'login.html', {
            'error': 'User or pass is incorrect'
            })
        else:
            login(request, user),
            return redirect('home')


# Cerrando sesion
@login_required
def signout(request):
    logout(request)
    return redirect('home')




# listar perfiles
@login_required
def perfiles(request):
    perfiles = PerfilTesisModel.objects.all()
    return render(request, 'perfiles_tesis.html',{
        'perfiles': perfiles
    })

@login_required
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


# Visualizar de tarea
@login_required
def perfil_detail(request, perfil_id):
    if request.method == 'GET':
        perfil = get_object_or_404(PerfilTesisModel, pk=perfil_id)
        form = PerfilForm(instance=perfil)
        return render(request, 'task_detail.html', {
            'perfil': perfil,
            'form': form
        })
    else:
        try:
            perfil = get_object_or_404(PerfilTesisModel, pk=perfil_id)
            form = PerfilForm(request.POST, instance=perfil)
            form.save()
            return redirect('perfiles')
        except ValueError:
            return render(request, 'task_detail.html', {
                'perfil': perfil,
                'form': form,
                'error': "Error al actualizar"
            })


#  Eliminar tarea
@login_required
def delete_perfil(request, perfil_id):
    perfil = get_object_or_404(PerfilTesisModel, pk=perfil_id)
    if request.method == 'POST':
        perfil.delete()
        return redirect('perfiles')


"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),


    path('perfiles/', views.perfiles , name='perfiles'),
    path('perfiles/create/', views.create_perfil , name='create_perfil'),
    path('perfiles/<int:perfiles_id>/', views.perfil_detail , name='perfil_detail'),
    path('perfiles/<int:perfiles_id>/delete/', views.delete_perfil, name='delete_perfil'),

    path('temas/', views.temas, name='temas'),



    path('tribunales', views.tribunales, name='tribunal'),



    path('sennalamiento', views.sennalamiento, name='sennalamiento'),



    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('login/signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),

]


"""django_init URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from apps.principal.views import inicio, crearPersona, editarPersona, eliminarPersona
from apps.principal.class_view import PersonaList,PersonaCreate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PersonaList.as_view(), name='index'),
    path('crear_persona/', PersonaCreate.as_view(), name='crear_Persona'),
    path('editarPersona/<int:id>/', editarPersona, name = 'editar_persona'),
    path('eliminarPersona/<int:id>/', eliminarPersona, name = 'eliminar_persona')
]

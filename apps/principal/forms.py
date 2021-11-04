from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        #fields = ('nombre', 'apellido',) esto es una tupla para los formularios precisos 
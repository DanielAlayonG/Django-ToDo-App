'''
Se importa las librerias necesarias para tener el template
del form
'''
from django import forms
from django.forms import ModelForm
from .models import *


#Las templates se deben ser class based
class TaskForm(forms.ModelForm):

    #En el class meta se define que model va a usar el form
    class Meta:

        #Se define qel modelo es el de las tareas
        model = Task

        '''
        Se pasan todos los campos del modelo
        tareas:
        Title
        Completed
        created
        '''
        fields = '__all__'
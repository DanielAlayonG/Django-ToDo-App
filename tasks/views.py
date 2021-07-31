from django.shortcuts import redirect, render
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()


    '''
    Se verifica que el metodo sea POST, es decir,
    que el formulario esta enviado información.
    '''
    if request.method == 'POST':
        form =  TaskForm(request.POST)
        '''
        El template verfica si el formulario
        esta correcto, si es asi lo "Guarda"
        sino lanza advertencias, al guardar
        el form se envia automaticamente
        a la base de datos
        '''
        
        if form.is_valid():
            form.save()
        '''
        Una vez el formulario se haya enviado
        se redirecciona a la misma pagina
        pero con el metodo GET
        '''
        return redirect('/')

    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'tasks/list.html', context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}

    return render(request, 'tasks/update_task.html', context)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {
        'task': task
    }

    return render(request, 'tasks/delete_task.html', context)
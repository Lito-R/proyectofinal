from django.shortcuts import render, redirect
from .models import Tarea, Actividad
from .forms import TareaForm, ActividadForm

def home(request):
    tareas = Tarea.objects.all()
    actividades = Actividad.objects.all()
    context = {'tareas':tareas}
    context2 = {'actividades':actividades}
    return render(request, 'todo/home.html', context)

#______________________________________________________________________________________


def agregartarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = TareaForm() or ActividadForm()
    context = {'form': form}
    return render(request, 'todo/agregartarea.html', context)

def eliminartarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect("home")

def editartarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == "POST":
        form = TareaForm(request.POST, instance= tarea)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TareaForm(instance=tarea)
    context = {"form": form}
    return render (request, "todo/editartarea.html", context)

#___________________________________________________________________________________________________________________

def agregaractividad(request):
    if request.method == "POST":
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = ActividadForm()
    context = {'form': form}
    return render(request, 'todo/agregaractividad.html', context)

def eliminaractividad(request, actividad_id):
    actividad = Actividad.objects.get(id=actividad_id)
    actividad.delete()
    return redirect("home")

def editaractividad(request, tarea_id):
    actividad = Actividad.objects.get(id=actividad_id)
    if request.method == "POST":
        form = ActividadForm(request.POST, instance= actividad)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ActividadForm(instance=actividad)
    context = {"form": form}
    return render (request, "todo/editaractividad.html", context)







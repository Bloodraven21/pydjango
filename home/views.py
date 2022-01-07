from django.shortcuts import redirect, render

from home.forms import TaskForm
from .models import *
from .models import *

# Create your views here.

def home(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)    

    context = {'tasks':tasks,'form':form}
    return render(request,'home.html',context)


def updatetask(request,pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method=='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect(home)    

    context = {'form':form}
    return render(request,'update.html',context)    


def deletetask(request,pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect(home)

    context = {'item':item}
    return render(request,'delete.html',context)
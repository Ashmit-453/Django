from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import Taskform,CreateUserForm
def home(request):
     q=Task.objects.all()
     context={'tasks':q}
     return render(request,'index.html',context)

def log(request):
    return render(request,'login.html')

def register(request):
     return render(request,'register.html')

def createTask(request):
     form=Taskform()
     if request.method=='POST':
          form=Taskform(request.POST)
          if form.is_valid():
               form.save()
               return redirect('viewform')
     context={'form':form}
     return render(request,'createtask.html',context)
 
def readtask(request):
     q=Task.objects.all()
     context={'t':q}
     return render(request,'readform.html',context)

def updateTask(request,p):
     task=Task.objects.get(id=p)
     form=Taskform(instance=task)
     if request.method=='POST':
          form=Taskform(request.POST,instance=task)
          if form.is_valid():
               form.save()
               return redirect('viewform')
     context={'form':form}
     return render(request,'updatetask.html',context)

def deleteTask(request,p):
     task=Task.objects.get(id=p)
     form=Taskform(instance=task)
     if request.method=='POST':
          task.delete()
          return redirect('viewform')
     context={'form':form}
     return render(request,'deletetask.html',context)

def Register(request):
    form = CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("registered successfully")  
    print("Form fields:", form.fields)              
    context={'form':form}
    return render(request,'register.html',context)      
     
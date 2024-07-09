from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('login/',views.log),
    path('register/',views.register),
    path('createtask/',views.createTask,name="create-task"),
    path('readtask/',views.readtask,name="viewform"),
    path('update_task/<int:p>/',views.updateTask,name="UpdateTask"),
    path('delete_task/<int:p>/',views.deleteTask,name="deleteTask"),
    path('register/',views.Register,name="register"),

]
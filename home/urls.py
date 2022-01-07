from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home' ),
    path('update/<str:pk>/',views.updatetask,name='update'),
    path('delete/<str:pk>/',views.deletetask,name='delete')
]

from django.urls import path
from employeeApp import views

urlpatterns = [
    path('', views.index),
    path('addUser/', views.addUser),
]

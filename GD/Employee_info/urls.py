from django.contrib import admin
from django.urls import path,include
from Employee_info import views

urlpatterns = [
    path('employee1/', views.first),
    path('employee2/', views.second)
]
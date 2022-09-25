from django.contrib import admin
from django.urls import path,include
from Student_info import views

urlpatterns = [
    path('student1/', views.first),
    path('student2/', views.second)
]
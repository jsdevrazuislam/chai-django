from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.jobs, name='jobs'),
  path('<int:job_id>/', views.job_details, name='job_details'),
  path('add/', views.add_job, name='add_job'),
] 
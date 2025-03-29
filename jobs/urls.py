from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.jobs, name='jobs'),
  path('<int:job_id>/', views.job_details, name='job_details'),
  path('add/', views.add_job, name='add_job'),
  path('view/', views.view_jobs, name='view_jobs'),
  path('<int:job_id>', views.edit_job, name='edit_job'),
  path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),

] 
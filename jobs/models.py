from django.db import models
from ckeditor.fields import RichTextField

class JobModel(models.Model):
    JOB_TYPES = [
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
        ('on-site', 'On Site'),
    ]
    
    EMPLOYEE_TYPE = [
        ('full-time', 'Full Time'),
        ('part-time', 'Part Time'),
        ('freelancer', 'Freelancer'),
    ]
    
    EMPLOYEE_RANGE = [
        ('small', '1-10'),
        ('medium', '10-50'),
        ('large', '50-200'),
    ]

    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logos/')
    company = models.CharField(max_length=250)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default='remote')
    employee_type = models.CharField(max_length=20, choices=EMPLOYEE_TYPE, default='full-time')
    body = RichTextField()
    min_salary = models.PositiveIntegerField()
    max_salary = models.PositiveIntegerField()
    location = models.CharField(max_length=250)
    employees_range = models.CharField(max_length=20, choices=EMPLOYEE_RANGE, default='small')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
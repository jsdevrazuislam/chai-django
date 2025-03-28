from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from datetime import date
from django.core.exceptions import ValidationError

def validate_birth_date(value):
    if value > date.today():
        raise ValidationError("Birth date cannot be in the feature!")

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract  = True

class User(BaseModel):
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    username = models.CharField(unique=True, max_length=50, blank=False, null=False)
    full_name = models.CharField(max_length=32, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False, validators=[
        MinLengthValidator(18, "Age Must be 18"),
        MaxLengthValidator(100, "Age must 18-100 ")
    ])
    email = models.EmailField(max_length=100, unique=True)
    profile_picture = models.ImageField(upload_to='profile/')
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=20,choices=GENDER, default='male')
    bio = models.TextField(null=True, blank=True)
    dob = models.DateField(blank=False, null=False, validators=[validate_birth_date])
    website = models.URLField()

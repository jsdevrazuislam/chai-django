from django import forms
from .models import JobModel
from ckeditor.fields import RichTextFormField


class JobForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg',
                'placeholder': 'Job Title'
            }),
            'company': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg',
                'placeholder': 'Company Name'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg',
                'placeholder': 'Job Location'
            }),
            'min_salary': forms.NumberInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg',
                'placeholder': 'Minimum Salary'
            }),
            'max_salary': forms.NumberInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg',
                'placeholder': 'Maximum Salary'
            }),
            'body': RichTextFormField(),
            'job_type': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'}),
            'employee_type': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'}),
            'employees_range': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'}),
            'logo': forms.FileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'}),
        }
# forms.py
from django import forms
from .models import Jobs

class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['job_application_date', 'job_title', 'job_type', 'company_name', 'applied_link', 'job_posted_date']
        widgets = {
            'job_application_date': forms.DateInput(attrs={'type': 'date'}),
            'job_posted_date': forms.DateInput(attrs={'type': 'date'}),
        }
        optional_fields = ['job_posted_date']
        
        def __init__(self, *args, **kwargs):
            super(JobForm, self).__init__(*args, **kwargs)
            for field in self.Meta.optional_fields:
                self.fields[field].required = False
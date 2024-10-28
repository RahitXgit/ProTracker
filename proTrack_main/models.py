from django.db import models

# Create your models here.
class Jobs(models.Model):
    job_application_date = models.DateField(verbose_name="Application Date", null=False)
    job_title = models.CharField(max_length=100, verbose_name="Role", null=False)
    
    JOB_TYPE_CHOICES = [
        ('internship', 'Internship'),
        ('job', 'Job'),
    ]
    
    job_type = models.CharField(
        max_length=10,
        choices=JOB_TYPE_CHOICES,
        verbose_name="Job Type",
        null=False
    )
    
    company_name = models.CharField(max_length=100, verbose_name="Company Name", null=False)
    applied_link = models.URLField(max_length=200, verbose_name="Application Link", null=False)
    job_posted_date = models.DateField(verbose_name="Job Posted Date")
    
    JOB_STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    job_status = models.CharField(max_length=10, choices=JOB_STATUS_CHOICES, verbose_name="Status", blank=True, null=False, default='pending')
    
    def __str__(self):
        return self.company_name

class AcceptedJobs(models.Model):
    job = models.OneToOneField(Jobs, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'job_status': 'accepted'})

    def __str__(self):
        return f"{self.job.company_name} - {self.job.job_title}"
    
class RejectedJobs(models.Model):
    job = models.OneToOneField(Jobs, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'job_status': 'rejected'})
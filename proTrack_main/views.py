from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Jobs, AcceptedJobs, RejectedJobs
from .forms import JobForm

def home(request):
    jobs = Jobs.objects.all().order_by('job_application_date')
    return render(request, 'home.html', {'jobs': jobs})

def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})

def delete_job(request, job_id):
    job = get_object_or_404(Jobs, id=job_id)
    job.delete()
    return redirect('home')

def update_status(request, job_id, status):
    job = get_object_or_404(Jobs, id=job_id)
    job.job_status = status
    job.save()
    if status == 'accepted':
        AcceptedJobs.objects.get_or_create(job=job)
    if status == 'rejected':
        RejectedJobs.objects.get_or_create(job=job)
    return redirect('home')

def accepted_jobs(request):
    jobs = AcceptedJobs.objects.all()
    return render(request, 'accepted_jobs.html', {'jobs': jobs})

def rejected_jobs(request):
    jobs = RejectedJobs.objects.all()
    return render(request, 'rejected_jobs.html', {'jobs': jobs})    

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import JobForm
from .models import JobModel



@login_required(login_url='/auth/login')
def jobs(request):
    jobs = JobModel.objects.all()
    return render(request, 'jobs.html', { 'jobs' : jobs})

@login_required(login_url='/auth/login')
def job_details(request, job_id):
    job = get_object_or_404(JobModel, pk=job_id)
    return render(request, 'job_details.html', {"job": job})

@login_required(login_url='/auth/login')
def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jobs')
    else:
        form = JobForm()
    
    return render(request, 'add_job.html', {'form': form})
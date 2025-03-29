from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import JobForm
from .models import JobModel
from django.http import JsonResponse


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
            job = form.save(commit=False)
            job.created_by = request.user 
            job.save()
            return redirect('jobs')
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})

@login_required(login_url='/auth/login')
def view_jobs(request):
    jobs = JobModel.objects.filter(created_by=request.user)
    return render(request, 'view_jobs.html', {'jobs': jobs})

@login_required(login_url='/auth/login')
def edit_job(request, job_id):
    job = get_object_or_404(JobModel, id=job_id, created_by=request.user) 
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs')
    else:
        form = JobForm(instance=job)

    return render(request, 'edit_job.html', {'form': form})

@login_required(login_url='/auth/login')
def delete_job(request, job_id):
    job = get_object_or_404(JobModel, id=job_id)

    if request.user == job.created_by:
        job.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False, "error": "Unauthorized"}, status=403) 
from django.shortcuts import render, redirect
from .forms import CandidateForm, JobForm
from .models import Candidate, Job
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.models import User

# Homepage 

def index(request):
	return render(request, 'index.html', {})


# Candidate
@login_required
def add_profile(request):
	newprofile = CandidateForm(request.POST or None)
	if newprofile.is_valid():
		newprofile.save()
		return redirect('/find_talent/')
	return render(request, 'addprofile.html', {'newprofile':newprofile})

def find_jobs(request):
	jobs = Job.objects.all()[::-1]
	full_time = Job.objects.filter(job_type="Full-time").count()
	part_time = Job.objects.filter(job_type="Part-time").count()
	internships = Job.objects.filter(job_type="Internship").count()
	return render(request, 'jobs.html', {'jobs':jobs, 'full_time': full_time, 'part_time': part_time, 'internships': internships})

def job_details(request, job_title):
	jobs = Job.objects.filter(job_title__contains=job_title)
	return render(request, 'job_details.html', {'jobs':jobs})


def find_internships(request):
	jobs = Job.objects.filter(job_type="Internship")
	full_time = Job.objects.filter(job_type="Full-time").count()
	part_time = Job.objects.filter(job_type="Part-time").count()
	internships = Job.objects.filter(job_type="Internship").count()
	return render(request, 'internships.html', {'jobs':jobs, 'full_time': full_time, 'part_time': part_time, 'internships': internships})

def recommended_jobs(request):
	jobs = Job.objects.filter(job_type="Full-time")
	full_time = Job.objects.filter(job_type="Full-time").count()
	part_time = Job.objects.filter(job_type="Part-time").count()
	internships = Job.objects.filter(job_type="Internship").count()
	return render(request, 'recommended_jobs.html', {'jobs':jobs, 'full_time': full_time, 'part_time': part_time, 'internships': internships})

# Job
@login_required
def add_job(request):
	newjob = JobForm(request.POST or None)
	if newjob.is_valid():
		newjob.save()
		return redirect('/find_jobs/')
	return render(request, 'addjob.html', {'newjob':newjob})

def find_talent(request):
	profiles = Candidate.objects.all()
	return render(request, 'profiles.html', {'profiles':profiles})
 

def talent_details(request, name):
	talent_details = Candidate.objects.filter(name__contains=name)
	return render(request, 'talent_details.html', {'talent_details':talent_details})


# login, registration, session 
def signin(request):
	if request.method == "POST":
		username = request.POST['username']
		password =  request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is None:
			return HttpResponse("Username or password is incorrect.")
		login(request, user)
		return redirect('/')
	else:
		form = UserForm()
	return render(request, 'login.html', {'form':form})

def signout(request):
	logout(request)
	return redirect('/login/')

def signup(request):
	if request.method=="POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		newuser = User.objects.create_user(
			first_name=first_name, 
			last_name=last_name,
			username=username,
			password=password,
			email=email
		)
		try:
			newuser.save()
			return redirect('/login/')
		except:
			return HttpResponse("Something went wrong.")
	form = UserRegistrationForm()
	return render(request, 'signup.html', {'form':form})


def search_jobs(request):
	search = request.GET.get('search')
	jobs = Job.objects.filter(
		job_location__contains=search
		)
	return render(request, 'search_results.html', {'jobs':jobs})

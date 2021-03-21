from django import forms
from .models import Job, Candidate
from django.contrib.auth.models import User

class JobForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = '__all__'

class CandidateForm(forms.ModelForm):
	class Meta:
		model = Candidate
		fields = '__all__'

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']

class UserRegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'email', 'first_name', 'last_name']
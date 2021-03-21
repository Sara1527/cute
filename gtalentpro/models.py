from django.db import models

class Candidate(models.Model):
	# Personal details
	name = models.CharField(max_length=60)
	phone = models.CharField(max_length=15, unique=True) # to avoid duplicate
	email = models.EmailField()
	# gender = models.CharField(
	# 	max_length=10,
	# 	choices=(
	# 		('Male', 'Male'),
	# 		('Female', 'Female'),
	# 		),
	# 	default="Male",
	# 	)
	city_of_residence = models.CharField(max_length=60, blank=True)
	about_me = models.TextField(blank=True)

	# Educational details 
	highest_education = models.CharField(max_length=60, blank=True)
	key_skills = models.CharField(max_length=120, blank=True)

	# Work experience
	total_experience = models.CharField(max_length=30, 
		choices=(
			('0', '0'),
			('1', '1'),
			('2', '2'),
			('3', '3'),
			('4', '4'),
			('5', '5'),
			('6', '5-10'),
			('11', '10+') 
			),
		default='0',
	)

	def __str__(self):
		return self.name

class Job(models.Model):
	job_title = models.CharField(max_length=120)
	employer_name = models.CharField(max_length=60, blank=True)
	job_location = models.CharField(max_length=120, blank=True)
	job_description = models.TextField(max_length=120, blank=True)
	job_type = models.CharField(max_length=60, 
		choices = (
			('Full-time', 'Full-time'),
			('Part-time', 'Part-time'),
			('Internship', 'Internship'),
			),
		default = "Full-time"
		)
	key_skills = models.CharField(max_length=60, blank=True)
	job_eligibility = models.CharField(max_length=60, blank=True)
	def __str__(self):
		return self.job_title
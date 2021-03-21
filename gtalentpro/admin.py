from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

class CandidateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ['name', 'highest_education', 'total_experience', 'city_of_residence']
	search_fields = ['name', 'phone', 'email']

class JobAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ['job_title', 'job_type', 'job_location', 'job_eligibility']

admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Job, JobAdmin)

admin.site.site_header = "Talent Pro"
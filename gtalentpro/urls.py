from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),

    # search
    path('search_jobs/', views.search_jobs),

    # candidate
    path('add_profile/', views.add_profile),
    path('find_jobs/', views.find_jobs),
    path('find_jobs/<str:job_title>/', views.job_details),
    path('find_internships/', views.find_internships),
    path('recommended_jobs/', views.recommended_jobs),

    # job
    path('add_job/', views.add_job),
    path('find_talent/', views.find_talent),
    path('find_talent/<str:name>/', views.talent_details),

    # login, registration, session
    path('login/', views.signin),
    path('logout/', views.signout),
    path('signup/', views.signup),
]
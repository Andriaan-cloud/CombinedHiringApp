from django.urls import path
from .import views
urlpatterns = [
    path('', views.job_requirement_survey, name='blog-job_requirement_survey'),
    path('about/', views.about, name='blog-about'),
]
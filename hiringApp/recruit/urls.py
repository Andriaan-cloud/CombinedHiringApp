from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.job_requirement_survey, name='blog-job_requirement_survey'),
    path("index/", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("success/", views.success, name="success"),
    path('profile/', views.profile, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

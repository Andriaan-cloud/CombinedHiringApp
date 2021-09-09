from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from recruit import views as user_views

urlpatterns = [

    path('', auth_views.LoginView.as_view(template_name='recruit/login.html'), name='login'),
    path('register', user_views.register, name='register'),
    path("require/", views.job_requirement_survey, name='blog-job_requirement_survey'),
    path('logout/', auth_views.LogoutView.as_view(template_name='recruit/logout.html'), name='logout'),
    path("index/", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("success/", views.success, name="success"),
    path('profile/', views.profile, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

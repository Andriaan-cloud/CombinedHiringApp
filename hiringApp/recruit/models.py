from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Response(models.Model):
    responsibilities = models.TextField()
    tech_skills = models.TextField()
    soft_skills = models.TextField()


class Document(models.Model):
    docfile = models.FileField(upload_to='documents')


class Profile(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=150)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    PROVINCE = (('Gauteng', 'Gauteng'), ('Mpumalanga', 'Mpumalanga'), ('KwaZulu Natal', 'KwaZulu Natal'),
                ('Free State', 'Free State'), ('Limpopo', 'Limpopo'), ('North West', 'North West'),
                ('Eastern Cape', 'Eastern Cape'), ('Western Cape', 'Western Cape'), ('Northern Cape', 'Northern Cape'))
    INDUSTRY = (('Business Services', 'Business Services'), ('Information Technology', 'Information Technology'),
                ('Financial Services', 'Financial Services'),
                ('Public Sector', 'Public Sector'), ('Energy & Natural Resources', 'Energy & Natural Resources'),
                ('Industrial / Manufacturing', 'Industrial / Manufacturing'),
                ('Retail', 'Retail'))
    SOCIAL = (('Facebook', 'Facebook'), ('LinkedIn', 'LinkedIn'), ('Twitter', 'Twtter'), ('Google+', 'Google+'),
              ('Email', 'Email'), ('Mindworx Website', 'Mindworx Website'))

    province = models.CharField(max_length=150, null=True, choices=PROVINCE)
    industry = models.CharField(max_length=150, null=True, choices=INDUSTRY)
    social = models.CharField(max_length=150, null=True, choices=SOCIAL)
    job_title = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str(self):
        return self.title

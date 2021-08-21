from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 150)
    surname = models.CharField(max_length = 150, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length = 150)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    PROVINCE = (('Gauteng', 'Gauteng'), ('Mpumalanga', 'Mpumalanga'),('KwaZulu Natal', 'KwaZulu Natal'),('Free State','Free State'),('Limpopo','Limpopo'),('North West','North West'),('Eastern Cape','Eastern Cape'),('Western Cape','Western Cape'),('Northern Cape','Northern Cape'))
    INDUSTRY = (('Business Services', 'Business Services'), ('Information Technology', 'Information Technology'),('Financial Services','Financial Services'),
                ('Public Sector','Public Sector'), ('Energy & Natural Resources','Energy & Natural Resources'), ('Industrial / Manufacturing','Industrial / Manufacturing'),
                ('Retail','Retail'))
    SOCIAL = (('Facebook', 'Facebook'), ('LinkedIn', 'LinkedIn'), ('Twitter', 'Twtter'), ('Google+','Google+'),('Email','Email'),('Mindworx Website','Mindworx Website')) 
    
    province = models.CharField(max_length = 150, null=True ,choices=PROVINCE)
    industry = models.CharField(max_length = 150, null=True ,choices=INDUSTRY)
    social = models.CharField(max_length = 150, null=True ,choices=SOCIAL)
    job_title = models.CharField(max_length=150, blank=True)
    bio  = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
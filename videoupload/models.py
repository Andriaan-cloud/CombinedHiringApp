from django.db import models

# Create your models here.
class videoupload(models.Model):
    caption = models.CharField(max_length=100)
    videoupload = models.FileField(upload_to="videoupload/%y")
    def __str__(self):
        return self.caption


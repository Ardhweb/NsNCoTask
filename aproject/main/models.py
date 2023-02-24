from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Client(models.Model):
    name = models.CharField(max_length=20, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

WORK_TYPE = [
    ('Youtube','Youtube'),
    ('Instagram','Instagram'),
    ('Other','Other'),
]
class Work(models.Model):
    link = models.URLField(unique=True)
    work_type = models.CharField(max_length=50,choices=WORK_TYPE)

    def __int__(self):
        return self.id
    

    
class Artist(models.Model):
    name = models.CharField(max_length=20, blank=True)
    work = models.ManyToManyField(Work)



from django.db import models

# Create your models here.

class User(models.Model):
    SEX = (
        ('M','Male'),
        ('F','Famale')
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=SEX)
    birthday = models.DateField(max_length=100)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.first_name 

class Job(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=50)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.job_name 

class Prueba(models.Model):
    pass
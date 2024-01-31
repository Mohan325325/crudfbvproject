from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    eno = models.IntegerField(unique=True)
    ename = models.CharField(max_length=20)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=120)

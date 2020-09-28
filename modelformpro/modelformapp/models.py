from django.db import models
class EmpData(models.Model):
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    location=models.CharField(max_length=100)

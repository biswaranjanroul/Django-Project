from django.db import models
class CommonData(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    class Meta:
        abstract=True
class Emp(CommonData):
      salary=models.IntegerField()
class Student(CommonData):
      marks=models.IntegerField()
class Customer(CommonData):
      sales=models.IntegerField()


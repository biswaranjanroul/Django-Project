from django.db import models

class EnquaryData(models.Model):
    firstname=models.CharField(max_length=100)
    middlename=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    location=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)


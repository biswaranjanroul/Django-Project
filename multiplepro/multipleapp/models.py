from django.db import models
class Customer(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=100)
    sales=models.IntegerField()
class Emp(models.Model):
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=100)
    salary=models.IntegerField()
class Student(models.Model):
     sid=models.AutoField(primary_key=True)
     sname=models.CharField(max_length=100)
     marks=models.IntegerField()
class Book(Customer,Emp,Student):
     bname=models.CharField(max_length=100)
     cost=models.IntegerField()


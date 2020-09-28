from django.db import models
class Student(models.Model):
    sname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
class Studentproxy(Student):
    class meta:
        proxy=True




from django.contrib import admin
from .models import Student,Studentproxy
class Adminstudent(admin.ModelAdmin):
    list_display = ['sname','location','email']
class Adminstudentproxy(admin.ModelAdmin):
    list_display = ['sname','location','email']
admin.site.register(Student,Adminstudent)
admin.site.register(Studentproxy,Adminstudentproxy)


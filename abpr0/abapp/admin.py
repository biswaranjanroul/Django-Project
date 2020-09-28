from django.contrib import admin
from.models import Customer,Student,Emp
class AdminStudent(admin.ModelAdmin):
    list_display = ['name','location','marks']
class AdminCustomer(admin.ModelAdmin):
    list_display = ['name','location','sales']
class AdminEmp(admin.ModelAdmin):
    list_display = ['name','location','salary']
admin.site.register(Emp,AdminEmp)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Student,AdminStudent)



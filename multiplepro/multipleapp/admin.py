from django.contrib import admin
from .models import Book,Student,Customer,Emp
class AdminCustomer(admin.ModelAdmin):
    list_display = ['cname','sales']
class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','marks']
class AdminEmp(admin.ModelAdmin):
    list_display = ['ename','salary']
class AdminBook(admin.ModelAdmin):
    list_display = ['bname','cost']
admin.site.register(Customer,AdminCustomer)
admin.site.register(Student,AdminStudent)
admin.site.register(Emp,AdminEmp)
admin.site.register(Book,AdminBook)

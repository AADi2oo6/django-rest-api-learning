from django.contrib import admin
from .models import student
# Register your models here.

# admin.site.register(student) # direct way of registration 

@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'branch')


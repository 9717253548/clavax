from django.contrib import admin
from student.models import StudentRecord

# Register your models here.

class VipinAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'fathers_name', 'phone_number', 'email')
    list_filter = ('student_name','phone_number','email')
    
admin.site.register(StudentRecord, VipinAdmin)

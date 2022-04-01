from django.contrib import admin
from .models import Classroom, Student

# Register your models here.

class ClassroomAdmin(admin.ModelAdmin):
    pass

class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Student, StudentAdmin)
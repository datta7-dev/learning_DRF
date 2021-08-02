from django.contrib import admin
from apiView.models import Teacher
# Register your models here.


# @admin.register(Teacher)
class teacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_id', 'name']


admin.site.register(Teacher, teacherAdmin)

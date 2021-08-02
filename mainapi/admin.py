from django.contrib import admin
from mainapi.models import Student
# Register your models here.


@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'marks']

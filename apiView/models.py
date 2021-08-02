from django.db import models

# Create your models here.


class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __int__(self):
        return self.teacher_id

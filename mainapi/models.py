from django.db import models
# Create your models here.


class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __int__(self):
        return self.roll_no

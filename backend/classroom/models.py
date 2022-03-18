from django.db import models

# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=120)
    student_capacity = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    admission_number = models.IntegerField(unique=True)
    is_qualified = models.BooleanField(default=False)
    averrage_score = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.first_name
        


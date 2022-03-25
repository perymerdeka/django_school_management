from django.db import models

# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=120)
    student_capacity = models.IntegerField()
    students = models.ManyToManyField("Student")

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    admission_number = models.IntegerField(unique=True)
    is_qualified = models.BooleanField(default=False)
    averrage_score = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return self.first_name

    # method
    def get_grade(self):
        if self.averrage_score < 40:
            return "Failed"
        elif 40 < self.averrage_score < 70:
            return "Pass"
        elif 70 < self.averrage_score < 100:
            return "Excellent"
        else:
            return "Error"

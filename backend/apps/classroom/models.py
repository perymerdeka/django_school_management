from django.db import models
from django.utils.text import slugify

from .validators import validate_negative

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
    averrage_score = models.IntegerField(unique=True, validators=[validate_negative])
    slug = models.SlugField(null=True, blank=True)

    def __str__(self) -> str:
        return self.first_name

    # method
    def get_grade(self):
        if 0 < self.averrage_score < 40:
            return "Failed"

        elif 40 < self.averrage_score < 70:
            return "Pass"
        elif 70 < self.averrage_score <= 100:
            return "Excellent"
        else:
            return "Error"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        return super(Student, self).save(*args, **kwargs)

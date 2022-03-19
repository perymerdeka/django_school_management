import random
from django.test import TestCase

from .models import Student

# Create your tests here.
class TestStudentModel(TestCase):
    def setUp(self) -> None:
        self.student1 = Student.objects.create(
            first_name="John",
            last_name="doe",
            admission_number=1,
            averrage_score=random.randint(41, 70),
        )
        return super().setUp()

    def test_create_student(self):
        payload = Student.objects.last()

        # test data
        self.assertEqual(payload.first_name, "John")
        self.assertEqual(payload.last_name, "doe")

    def test_student_can_be_created(self):
        self.assertEqual(self.student1.first_name, "John")

    def test_pass_grade(self):
        self.assertEqual(self.student1.get_grade(), "Pass")

    def test_excelent_grade(self):
        student_data = Student.objects.create(
            first_name="John",
            last_name="doe",
            admission_number=2,
            averrage_score=random.randint(70, 100),
        )
        self.assertEqual(student_data.get_grade(), "Excellent")

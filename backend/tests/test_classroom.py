import random
from django.test import TestCase
from mixer.backend.django import mixer

from classroom.models import Student

# Create your tests here.
class TestStudentModel(TestCase):
    def setUp(self) -> None:
        self.student1 = mixer.blend(Student, first_name="John", last_name="doe")
        return super().setUp()

    def test_create_student(self):
        payload = Student.objects.last()

        # test data
        self.assertEqual(payload.first_name, "John")
        self.assertEqual(payload.last_name, "doe")

    def test_student_can_be_created(self):
        self.assertEqual(self.student1.first_name, "John")

    def test_pass_grade(self):
        student = mixer.blend(
            Student, first_name="Tom", averrage_score=random.randint(50, 71)
        )
        self.assertEqual(student.get_grade(), "Pass")

    def test_excelent_grade(self):
        student = mixer.blend(
            Student, first_name="Tom", averrage_score=random.randint(70, 100)
        )
        self.assertEqual(student.get_grade(), "Excellent")

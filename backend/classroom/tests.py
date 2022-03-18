from django.test import TestCase
from .models import Student

# Create your tests here.
class TestStudentModel(TestCase):
    def test_create_student(self):
        student1 = Student.objects.create(first_name="John", last_name="doe", admission_number=1)
        payload = Student.objects.last()

        # self test
        self.assertEqual(payload.first_name, "John")
        self.assertEqual(payload.last_name, "doe")

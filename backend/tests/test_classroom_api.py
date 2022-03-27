from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from mixer.backend.django import mixer

from classroom.models import Student

class StudentAPITest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.student_data = mixer.blend(Student, first_name="Tom")
        return super().setUp()

    def test_student_list_api(self):
        url: str = reverse('student_list')
        response = self.client.get(url, format="json")
        payload = response.json()
        
        assert response.status_code == 200
        assert response.json != None
        assert len(payload) == 1
        
        for data in payload:
            assert data['first_name'] == "Tom"


    
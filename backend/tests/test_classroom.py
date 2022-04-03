from django.test import TestCase
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from rest_framework import status


from apps.classroom.models import Classroom

class TestClassroomAPIView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        return super().setUp()

    def test_classroom_queryset_empty_data(self):
        # sourcery skip: class-extract-method

        url = reverse("class_qs_api", kwargs={"student_capacity": 25})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_202_ACCEPTED
        payload = response.json()
        assert payload['classroom_data'] == []
        assert payload['number_of_classes'] == 0
    
    def test_classroom_queryset_data(self):
        classroom = mixer.blend(Classroom, student_capacity=25)
        url = reverse("class_qs_api", kwargs={"student_capacity": 25})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_202_ACCEPTED
        payload = response.json()
        assert payload['classroom_data'][0]['student_capacity'] == 25
        assert payload['number_of_classes'] == 1
        


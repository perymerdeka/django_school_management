from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from mixer.backend.django import mixer

from classroom.models import Student


class StudentAPITest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.student_data = mixer.blend(
            Student,
            first_name="Tom",
            last_name="Doe",
            admission_number=1,
            is_qualified=False,
        )
        return super().setUp()

    def test_student_list_api(self):
        url: str = reverse("student_list")
        response = self.client.get(url, format="json")
        payload = response.json()

        assert response.status_code == 200
        assert response.json != None
        assert len(payload) == 1

        for data in payload:
            assert data["first_name"] == "Tom"

    def test_create_student_api(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "admission_number": 10,
            "is_qualified": False,
            "averrage_score": 90,
        }
        url: str = reverse("create_student")
        response = self.client.post(url, data=data, format="json")
        assert response.status_code == status.HTTP_201_CREATED

    def test_detail_student_api(self):
        url: str = reverse("detail_student", args=[self.student_data.id])
        response = self.client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK

        payload = response.json()
        
        # test data
        assert payload['id'] == self.student_data.id
        assert payload['first_name'] == self.student_data.first_name
        assert payload['last_name'] == self.student_data.last_name
        assert payload['admission_number'] == self.student_data.admission_number
        assert payload['is_qualified'] == self.student_data.is_qualified
        assert payload['slug'] == self.student_data.slug




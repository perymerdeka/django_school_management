from django.urls import path, include
from rest_framework.authtoken import views  

from .views import (
    StudentCreateAPIView,
    StudentDeleteAPIView,
    StudentListAPIView,
    StudentRetrieveAPIView,
    ClassroomNumberAPIView,
)

urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path("students/", StudentListAPIView.as_view(), name="student_list"),
    path("students/create/", StudentCreateAPIView.as_view(), name="create_student"),
    path(
        "students/detail/<int:pk>",
        StudentRetrieveAPIView.as_view(),
        name="detail_student",
    ),
    path(
        "students/delete/<int:pk>",
        StudentDeleteAPIView.as_view(),
        name="delete_student",
    ),
    # classroom url
    path(
        "classroom/<int:student_capacity>/",
        ClassroomNumberAPIView.as_view(),
        name="class_qs_api",
    ),
]

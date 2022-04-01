from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)

from apps.classroom.models import Student
from .serializers import (
    CreateStudentSerializer,
    DestroyStudentSerializer,
    RetrieveStudentSerializer,
    StudentSerializer,
)


class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    model = Student
    serializer_class = StudentSerializer


class StudentCreateAPIView(CreateAPIView):
    serializer_class = CreateStudentSerializer
    model = Student
    queryset = Student.objects.all()


class StudentRetrieveAPIView(RetrieveAPIView):
    serializer_class = RetrieveStudentSerializer
    model = Student
    queryset = Student.objects.all()


class StudentDeleteAPIView(DestroyAPIView):
    serializer_class = DestroyStudentSerializer
    model = Student
    queryset = Student.objects.all()

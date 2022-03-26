from rest_framework.generics import ListAPIView

from classroom.models import Student
from .serializers import StudentSerializer

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    model = Student
    serializer_class = StudentSerializer
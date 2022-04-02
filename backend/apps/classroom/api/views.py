from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from apps.classroom.models import Student, Classroom
from .serializers import (
    ClassroomNumberSerializer,
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


class ClassroomNumberAPIView(APIView):
    queryset = Student.objects.all()
    model = Classroom
    serializer_class = ClassroomNumberSerializer

    def get(self, *args, **kwargs):

        url_number = self.kwargs.get("student_capacity")
        print(url_number, "student_capacity")

        classroom_qs = Classroom.objects.filter(student_capacity__gte=url_number)
        number_of_classes = classroom_qs.count()

        serializer = ClassroomNumberSerializer(classroom_qs, many=True)

        if serializer.is_valid:
            return Response(
                {
                    "classroom_data": serializer.data,
                    "number_of_classes": number_of_classes,
                },
                status=status.HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                {"Error": "Could not serialize data"},
                status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
            )

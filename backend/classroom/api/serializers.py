from rest_framework.serializers import ModelSerializer

from classroom.models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class CreateStudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class RetrieveStudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class DestroyStudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

from django.urls import path, include

from .views import StudentListAPIView

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('students/', StudentListAPIView.as_view(), name="student_list"),
]
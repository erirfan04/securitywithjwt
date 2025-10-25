from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Course
from accounts.decorators import role_required
from django.http import HttpResponse
"""
@api_view(["GET"])
@permission_classes([RolePermission(allowed_roles=["student", "instructor", "admin"])])
def list_courses(request):
    courses = Course.objects.all().values("id", "name", "description")
    return Response(list(courses))
    Hello how are you?
    i am good how about you?
"""
@api_view(["GET"])
@role_required(["student", "instructor", "admin"])
def list_courses(request):
   courses = Course.objects.all().values("id", "name", "description")
   return Response(list(courses))


@api_view(["POST"])
@role_required([ "instructor", "admin"])
def create_course(request):
    name = request.data.get("name")
    description = request.data.get("description")
    course = Course.objects.create(
        name=name, description=description, created_by=request.user
    )
    return Response({"message": "Course created", "course_id": course.id})





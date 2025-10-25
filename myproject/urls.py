"""

"""
import debug_toolbar
from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import user_profile
from courses.views import list_courses, create_course
from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path("__debug__/", include(debug_toolbar.urls)),
    

    # JWT Endpoints
    # JWT Endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Protected route
    path("api/profile/", user_profile, name="user_profile"),
    # Courses (RBAC protected)
    path("api/courses/", list_courses, name="list_courses"),
    path("api/courses/create/", create_course, name="create_course"),
    
]


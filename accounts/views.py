from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

"""
@permission_classes([IsAuthenticated])

This ensures only authenticated users can access this view.

Authentication here usually means:

User provided a valid JWT token in Authorization header.

If a user is not authenticated → DRF automatically returns 401 Unauthorized.

3. def user_profile(request):

A normal Python function (view) that DRF will call when the route is accessed.

request → contains all request info, including the logged-in user (request.user).

4. serializer = UserSerializer(request.user)

request.user → DRF sets this based on authentication.

If JWT token is valid, request.user is the corresponding User object.

UserSerializer → A DRF serializer that converts the User object into JSON-friendly format.

"""
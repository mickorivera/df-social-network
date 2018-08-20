from rest_framework import generics

from socialnetworkauth.models import User
from socialnetworkauth.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    """List all users or create new user."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete user."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

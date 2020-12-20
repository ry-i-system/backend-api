"""
Users views modules
"""
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from users.serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
    """ List class """
    permission_classes = (permissions.IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Detail class """
    permission_classes = (permissions.IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

"""
Posts views modules
"""
from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer

# ListCreateAPIView -> read-write endpoint
class PostList(generics.ListCreateAPIView):
    """ List class """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# RetrieveUpdateDestoryAPIView -> ALlows read, update, delete
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Detail class """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

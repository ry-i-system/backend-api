"""
Posts serializers modules
"""
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """ Serializers class """

    class Meta:
        """ Meta class """
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post

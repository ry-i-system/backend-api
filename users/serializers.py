"""
Users serializers modules
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """ Serializer class """

    class Meta:
        """ Meta class """
        model = get_user_model()
        fields = ('id', 'username',)

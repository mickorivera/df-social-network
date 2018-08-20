from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer class for model `User`"""
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'is_active')

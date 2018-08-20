from rest_framework import serializers

from accounts.models import User
from feeds.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer class for model `Post`"""

    class Meta:
        model = Post
        fields = ('author', 'content', 'datetime_created',)

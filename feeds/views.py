from rest_framework import generics

from feeds.models import Post
from feeds.serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """List all posts or create new post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

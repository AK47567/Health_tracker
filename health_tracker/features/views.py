from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import CommunityPost, Like
from .serializers import CommunityPostSerializer, LikeSerializer


class CommunityPostCreateAPIView(generics.CreateAPIView):
    queryset = CommunityPost.objects.all()
    serializer_class = CommunityPostSerializer


class LikePost(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = CommunityPost.objects.get(pk=post_id)
        serializer.save(post=post)
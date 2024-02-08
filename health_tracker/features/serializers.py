

from rest_framework import serializers
from .models import CommunityPost, Like

class CommunityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityPost
        fields = ['subject', 'body']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
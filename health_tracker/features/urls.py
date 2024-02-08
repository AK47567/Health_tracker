
from django.urls import path
from .views import CommunityPostCreateAPIView, LikePost

urlpatterns = [
    path('posts/', CommunityPostCreateAPIView.as_view(), name='community_post_create'),
    path('like/<int:post_id>/', LikePost.as_view(), name='like_post'),

]
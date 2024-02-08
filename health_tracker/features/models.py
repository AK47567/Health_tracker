


from django.db import models
from django.contrib.auth.models import User

class CommunityPost(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', through='Like')

    def total_likes(self):
        return self.likes.count()

# models.py

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

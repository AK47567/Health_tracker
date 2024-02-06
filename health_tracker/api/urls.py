from django.urls import path
from .views import UserProfileList

urlpatterns = [
    path('user-profiles/', UserProfileList.as_view(), name='user-profile-list'),
]

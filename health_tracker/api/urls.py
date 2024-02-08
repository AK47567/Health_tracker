from django.urls import path, include
from .views import UserProfileList

urlpatterns = [
    path('user-profiles/', UserProfileList.as_view(), name='user-profile-list'),
    path('community/', include('features.urls')),
]

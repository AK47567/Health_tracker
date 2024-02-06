from rest_framework import generics
from .models import UserList, BMI
from .serializers import UserProfileSerializer, BMISerializer

from rest_framework.response import Response
from rest_framework import status

class UserProfileList(generics.ListCreateAPIView):
    queryset = UserList.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        user_profiles = self.queryset.filter(user=request.user)
        serializer = self.serializer_class(user_profiles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BMIList(generics.ListCreateAPIView):
    queryset = BMI.objects.all()
    serializer_class = BMISerializer
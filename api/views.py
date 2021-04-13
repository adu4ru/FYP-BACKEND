from django.shortcuts import render

# Create your views here.
from .serializers import UserSerializer, BloodSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from WebApp.models import Blood



class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    # permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            
            status=status.HTTP_400_BAD_REQUEST
            
        )

class BloodRecordView(APIView):
    def get(self, request):
        print("Hello")
        blood = Blood.objects.all()
        # print(blood)
        # print(blood)
        serializer = BloodSerializer(blood, many=True)
        # print(serializer)
        return Response(serializer.data)
        # print(serializer.data)

    def post(self, request):
        pass
        serializer = BloodSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )
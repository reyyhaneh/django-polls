from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .serializers import UserRegistrationSerializer, UserloginSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegistrationView(APIView):

    def post(self, request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User registerde successfully."
            }, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserloginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password = password)
            
            if user:
                login(request, user)
                return Response({
                    "message": "Login successfull."
                }, status = status.HTTP_200_OK)
            return Response({
                "error": "Invalid credentilals"
            }, status = status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

    
        


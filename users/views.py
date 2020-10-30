from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from .serializers import RegisterUserSerializer

class SignupAPIView(GenericAPIView):
    """
    """
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginAPIView(APIView):
    """
    """
    permission_classes = [AllowAny,]

    def post(self, request):

        user = authenticate(
            username=request.data['username'], 
            password=request.data['password']
        )
        if user:
            token = Token.objects.create(user=user)
            return Response({'token':token.key}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)





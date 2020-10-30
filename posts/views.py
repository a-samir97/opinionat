from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status 



class PostAPIView(APIView):
    """
    """
    def get(self, request):
        pass

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def put(self, request):
        pass


class CommentAPIView(APIView):
    """
    """
    def get(self, request):
        pass

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def put(self, request):
        pass


class UpvoteAPIView(APIView):
    """
    """
    def post(self, request):
        pass

class DownvoteAPIView(APIView):
    """
    """
    def post(self, request):
        pass
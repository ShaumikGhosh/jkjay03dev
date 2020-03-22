from rest_framework.views import APIView
from api.serializers import SignUpSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


class SignupUser(APIView):

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = "Account successfully registered!"
            return Response({"message" : message}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
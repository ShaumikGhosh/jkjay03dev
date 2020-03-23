from rest_framework.views import APIView
from api.serializers import SignUpSerializer, LoginSerializer, UserPostSerializer
from django.contrib.auth import login, logout
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from api.models import UserPost


class SignupUser(APIView):

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = "Account successfully registered!"
            return Response({"message" : message}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)


class LogoutUser(APIView):

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreatePost(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def get(self, request, format=None):
        posts = UserPost.objects.all()
        serializer = UserPostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = UserPostSerializer(data=request.data)

        try:
            image = request.data['post_image']
        except Exception:
            image = None

        if serializer.is_valid():
            serializer.save(user=request.user, post_image=image)
            message = "Post created successfully!"
            return Response({"message": message}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePost(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def get_object(self, pk, user):
        try:
            return UserPost.objects.get(pk=pk, user=user)
        except UserPost.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        data = self.get_object(pk, request.user)
        serializer = UserPostSerializer(data)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk, request.user)
        serializer = UserPostSerializer(post, data=request.data)

        try:
            image = request.data['post_image']
        except Exception:
            image = None
        is_active = request.data['is_active']

        if serializer.is_valid():
            serializer.save(post_image=image, is_active=is_active)
            message = "Data successfully updated!"
            return Response({"message": message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = self.get_object(pk, request.user)
        data.delete()
        message = "Your post is deleted!"
        return Response({"message":message})
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

    def get_object(self, id, user):
        try:
            return UserPost.objects.get(id=id, user=user)
        except UserPost.DoesNotExist:
            raise Http404

    def get(self, request, id):
        post = self.get_object(id, request.user)
        serializer = UserPostSerializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = self.get_object(id, request.user)
        serializer = UserPostSerializer(post, data=request.data)

        try:
            image = request.data['post_image']
        except Exception:
            image = None

        if serializer.is_valid():
            serializer.save(user=request.user, post_image=image)
            message = "Data successfully inserted!"
            return Response({"message": message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

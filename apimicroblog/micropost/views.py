from django.shortcuts import render
from rest_framework import generics, status
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated] # Requiere autenticación
    serializer_class = PostSerializer
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        serializer.save(likes=self.get_object().likes.all())

class PostFilterView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Post.objects.filter(title__icontains=name)
    
class LikeListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated] # Requiere autenticación
    serializer_class = LikeSerializer
    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Both username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({'access_token': access_token}, status=status.HTTP_201_CREATED)
class TokenObtainPairView(TokenObtainPairView):
    pass
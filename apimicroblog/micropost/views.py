from django.shortcuts import render
from rest_framework import generics
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer

# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
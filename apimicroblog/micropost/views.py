from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostFilterView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Post.objects.filter(title__icontains=name)
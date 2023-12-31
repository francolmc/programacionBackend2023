from rest_framework import serializers
from .models import Post, Like

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Like
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    likes = LikeSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
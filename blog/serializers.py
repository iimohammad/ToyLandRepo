from rest_framework import serializers
from .models import Post, Comment, Category, Media
from user_panel.serializers import CustomUserSerializer


class CategorySerialziers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class PostSerializers(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'owner']


class CommentSerializers(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'author']


class AdminCommentSerializers(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'author', 'is_active']



class MediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'post', 'caption', 'media']

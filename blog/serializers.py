from rest_framework import serializers
from .models import Post, Comment, Category, Media


class CategorySerialziers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'owner']


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'author']


class MediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'post', 'caption', 'media']

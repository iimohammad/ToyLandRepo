from rest_framework import serializers
from .models import Post, Comment, Category, Image, Video


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


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'post', 'caption', 'image']


class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'post', 'caption', 'video']

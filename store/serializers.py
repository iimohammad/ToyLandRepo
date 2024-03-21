from rest_framework import serializers
from user_panel.serializers import CustomUserSerializer
from store.models import Category, Comment, Product, Media


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class CommentSerializers(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'product', 'text', 'author')


class AdminCommentSerializers(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'product', 'text', 'author', 'is_active')


class MediaSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['product', 'caption', 'media']



class ProductSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category']

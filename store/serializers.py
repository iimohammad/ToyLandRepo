from rest_framework import serializers

from store.models import Category, Comment, Product, Media


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'product', 'text', 'author')


class MediaSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['product', 'caption', 'media']



class ProductSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category']

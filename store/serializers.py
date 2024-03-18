from rest_framework import serializers

from store.models import Category, Comment, Product, Video, Image


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'product', 'text', 'author')


class VideoSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['product', 'caption', 'video']


class ImageSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['product', 'caption', 'image']


class ProductSerialziers(serializers.ModelSerializer):
    image = ImageSerialziers(many=True, read_only=True)
    category_data = CategorySerializers(read_only=True)

    class Meta:
        model = Product
        fileds = ['id', 'name', 'description', 'price', 'image', 'category', 'category_data']

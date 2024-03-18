from rest_framework import viewsets, permissions
from .serializers import ProductSerialziers, CategorySerializers, CommentSerializers, VideoSerialziers, ImageSerialziers
from .models import Product, Category, Comment, Video, Image

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerialziers
    permission_classes = [permissions.IsAdminUser]
    search_fields = ('name', 'description')

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [permissions.IsAdminUser]
    search_fields = ('name', 'description')

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(is_active=True).order_by('-pk')
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAdminUser]
    search_fields = ('text',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerialziers
    permission_classes = [permissions.IsAdminUser]
    

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerialziers
    permission_classes = [permissions.IsAdminUser]

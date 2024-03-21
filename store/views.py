from rest_framework import viewsets, permissions
from .serializers import ProductSerialziers, CategorySerializers, CommentSerializers, MediaSerialziers
from .models import Product, Category, Comment, Media

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

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerialziers
    permission_classes = [permissions.IsAdminUser]


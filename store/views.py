from rest_framework import viewsets, permissions
from .serializers import AdminCommentSerializers, ProductSerialziers, CategorySerializers, CommentSerializers, MediaSerialziers
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = ('text',)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.user.is_staff:
            return AdminCommentSerializers
        return CommentSerializers
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Comment.objects.all()
        return Comment.objects.filter(is_active=True, author=self.request.user).order_by('-pk')


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerialziers
    permission_classes = [permissions.IsAdminUser]


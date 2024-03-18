from .serializers import *
from .models import *
from rest_framework import viewsets, permissions


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialziers
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ('name',)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ('title', 'content')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializers
    queryset = Comment.objects.filter(is_active=True).order_by('-pk')
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ('post',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializers
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ('caption',)

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ('caption',)
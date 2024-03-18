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

    def perform_create_or_update(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_create(self, serializer):
        self.perform_create_or_update(serializer)

    def perform_update(self, serializer):
        self.perform_create_or_update(serializer)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ('post',)

    def get_queryset(self):
        return Comment.objects.filter(is_active=True, author=self.request.user).order_by('-pk')

    def perform_create(self, serializer):
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
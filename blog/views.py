from .serializers import *
from .models import *
from rest_framework import viewsets, permissions
from .permissions import IsAdminOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialziers
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ('name',)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ('title', 'content')


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ('post',)

    def get_queryset(self):
        return Comment.objects.filter(is_active=True, author=self.request.user).order_by('-pk')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializers
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ('caption',)
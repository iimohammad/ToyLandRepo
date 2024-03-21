from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, CategoryViewSet, CommentViewSet, MediaViewSet

router = DefaultRouter()

router.register('Product', ProductViewSet, basename='Product')
router.register('Category', CategoryViewSet, basename='Category')
router.register('CommentStore', CommentViewSet, basename='CommentStore')
router.register('MediaStore', MediaViewSet, basename='MediaSote')

urlpatterns = [
    path('', include(router.urls)),
]

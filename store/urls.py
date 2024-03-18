from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, CategoryViewSet, CommentViewSet, VideoViewSet, ImageViewSet

router = DefaultRouter()

router.register('Product', ProductViewSet, basename='Product')
router.register('Category', CategoryViewSet, basename='Category')
router.register('Comment', CommentViewSet, basename='Comment')
router.register('Video', VideoViewSet, basename='Video')
router.register('Image', ImageViewSet, basename='Image')

urlpatterns = [
    path('', include(router.urls)),
]

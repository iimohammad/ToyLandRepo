from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, CategoryViewSet, CommentViewSet, MediaViewSet

router = DefaultRouter()

router.register('Product', ProductViewSet, basename='Product')
router.register('Category', CategoryViewSet, basename='Category')
router.register('Comment', CommentViewSet, basename='Comment')
router.register('Media', MediaViewSet, basename='Media')

urlpatterns = [
    path('', include(router.urls)),
]

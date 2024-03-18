from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CommentViewSet, ImageViewSet, PostViewSet, VideoViewSet
from django.urls import path, include

router = DefaultRouter()  

router.register('category', CategoryViewSet, basename='category') 
router.register('Post',PostViewSet,basename='Post')
router.register('Comment',CommentViewSet,basename='Comment')
router.register('Image',ImageViewSet,basename='Image')
router.register('Video',VideoViewSet,basename='Video')

urlpatterns = [
    path('', include(router.urls)),  
]

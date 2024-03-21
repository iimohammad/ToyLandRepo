from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CommentViewSet, MediaViewSet, PostViewSet
from django.urls import path, include

router = DefaultRouter()  

router.register('category', CategoryViewSet, basename='category') 
router.register('Post',PostViewSet,basename='Post')
router.register('Comment',CommentViewSet,basename='Comment')
router.register('Media',MediaViewSet,basename='Media')

urlpatterns = [
    path('', include(router.urls)),  
]

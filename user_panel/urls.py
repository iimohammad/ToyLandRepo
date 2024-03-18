from django.urls import path
from user_panel.views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='user-profile')
urlpatterns = router.urls
urlpatterns += [
    path('register/', RegisterUserApi.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]

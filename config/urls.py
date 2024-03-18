from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .local_settings import *

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),

    # App URLS
    path('user_panel/', include('user_panel.urls'), name='blog'),
    path('blog/', include('blog.urls'), name='blog'),
    path('finance/', include('blog.urls'), name='blog'),
    # path('purchase/', include('blog.urls'), name='blog'),
    path('store/', include('blog.urls'), name='blog'),

    # Authentication URLS
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls')),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .local_settings import *
from home.views import home

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
    # App URLS
    path('', home),
    path('user_panel/', include('user_panel.urls'), name='blog'),
    path('blog/', include('blog.urls'), name='blog'),
    path('finance/', include('finance.urls'), name='finance'),
    path('purchase/', include('purchase.urls'), name='purchase'),
    path('store/', include('store.urls'), name='store'),

    # Authentication URLS
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls')),
]

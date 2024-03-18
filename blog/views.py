from .serializers import *
from .models import *
from rest_framework import viewsets, permissions


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all
    serializer_class = CategorySerialziers
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ('name',)





from rest_framework import viewsets, permissions
from .models import PurchaseOrder, PurchaseOrderItem
from finance.serializers import PurchaseOrderItemSerializer, PurchaseOrderSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()
    permission_classes = [permissions.IsAdminUser]
    filterset_fields = ('user',)

class PurchaseOrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseOrderItem
    queryset = PurchaseOrderItem.objects.all()
    permission_classes = [permissions.IsAdminUser]
from rest_framework import viewsets, permissions
from .models import PurchaseOrder, PurchaseOrderItem
from finance.serializers import PurchaseOrderItemSerializer, PurchaseOrderSerializer


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class PurchaseOrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseOrderItemSerializer 
    queryset = PurchaseOrderItem.objects.all()
    permission_classes = [permissions.IsAdminUser]

from rest_framework import serializers
from .models import PurchaseOrder, PurchaseOrderItem
from store.serializers import *
from user_panel.serializers import UserSerializer


class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price']
        read_only_fields = ['id']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    items = PurchaseOrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = PurchaseOrder
        fields = ['id', 'creator', 'created_at', 'items', 'total_price']
        read_only_fields = ['id', 'created_at', 'total_price']

    def get_total_price(self, obj):
        total = 0
        for item in obj.items.all():
            total += item.quantity * item.price
        return total

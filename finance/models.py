from django.db import models
from store.models import Product
from user_panel.models import CustomUser

class PurchaseOrder(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase Order {self.id}"

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.quantity * item.price
        return total

class PurchaseOrderItem(models.Model):
    order = models.ForeignKey(PurchaseOrder, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='purchase_order_items')
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Purchase Order Item {self.id}"

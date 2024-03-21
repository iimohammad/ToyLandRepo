from django.contrib import admin
from .models import wallet, Cart, CartItem


@admin.register(wallet)
class walletAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'balance', 'created_at']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'created_at']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity']

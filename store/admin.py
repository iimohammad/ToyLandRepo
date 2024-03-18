from django.contrib import admin
from .models import Product, Category, Comment, Video, Image

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    search_fields = ['name', 'description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'product', 'author', 'is_active', 'created_at']
    search_fields = ['text']
    list_filter = ['is_active']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['caption', 'get_post']
    search_fields = ['caption']

    def get_post(self, obj):
        return obj.post  

    get_post.short_description = 'Post'

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'product']
    search_fields = ['caption']

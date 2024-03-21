from django.contrib import admin
from .models import Category, Post, Comment, Media


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'owner', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['category']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'post', 'author', 'is_active', 'created_at']
    search_fields = ['content']
    list_filter = ['is_active']


@admin.register(Media)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption', 'post']
    search_fields = ['caption']

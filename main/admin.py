from django.utils.html import mark_safe
from django.contrib import admin

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class ContentInline(admin.StackedInline):
    model = Content
    extra = 1

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","image_tag", "author", "reading_time", "views", "created_at", "published", "important", "category")
    search_fields = ["title", 'author','intro']
    list_filter = ("author", "important", "published", "category", "tags",)
    date_hierarchy = 'created_at'
    inlines = [ContentInline, CommentInline]
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px"/>')
        return "(No image)"





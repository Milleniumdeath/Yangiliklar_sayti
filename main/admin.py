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
    list_display = ("title", "author", "reading_time", "views", "created_at", "published", "important", "category")
    search_fields = ["title", 'author','intro']
    list_filter = ("author", "important", "published", "category", "tags",)
    date_hierarchy = 'created_at'
    inlines = [ContentInline, CommentInline]





from django.contrib import admin
from .models import Post, Comment, UserProfile, PostImage


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1
    fields = ['image', 'caption', 'order']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'website']
    search_fields = ['user__username', 'bio', 'location']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'location', 'created_at', 'total_likes', 'image_count']
    list_filter = ['created_at', 'updated_at', 'author', 'location']
    search_fields = ['title', 'content', 'location']
    readonly_fields = ['total_likes']
    inlines = [PostImageInline]
    
    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = 'Images'


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'caption', 'order']
    list_filter = ['post__author', 'post__created_at']
    search_fields = ['post__title', 'caption']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['content']

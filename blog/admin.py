from django.contrib import admin
from .models import Post
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # Displays the properties (title/slug/status/created date)
    list_display = ('title', 'slug', 'status', 'created_on')
    # Search field for content and title
    searc_fields = ['title', 'content']
    # Automatically populates the slug field
    prepopulated_fields = {'slug': ('title', )}
    # filters the posts by status and created date
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    searcg_fields = ('name', 'email', 'body')
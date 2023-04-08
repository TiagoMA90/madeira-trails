from django.contrib import admin
from .models import Post
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin

# Class for the Post
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # Displays the properties for the Post (title/slug/status/created date)
    list_display = ('title', 'slug', 'status', 'created_on')
    # Search field for content and title
    search_fields = ['title', 'content']
    # Automatically populates the slug field
    prepopulated_fields = {'slug': ('title',)}
    # filters the posts by status and created date
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)

# Class for the Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Displays the properties for the Comment (name/body/status/created date)
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    # Searchable by the (name/email/body)
    search_fields = ('name', 'email', 'body')
    # Approves the comment
    actions = ['approve_comments']

    # Function for approval of the Comment
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
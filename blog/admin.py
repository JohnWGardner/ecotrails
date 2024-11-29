from django.contrib import admin
from .models import BlogPost, BlogPostComments
from django_summernote.admin import SummernoteModelAdmin

class BlogPostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(BlogPost) #This registion allows me to create, update and delete blog posts from the admin panel.
admin.site.register(BlogPostComments) #This registion allows users to create, comments on my blog posts.


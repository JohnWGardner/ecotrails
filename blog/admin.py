from django.contrib import admin
from .models import BlogPost, BlogPostComments
from django_summernote.admin import SummernoteModelAdmin

@admin.register(BlogPost) # This decorator registers the custom admin class for BlogPost, compared to the traditional approach of registering a model (as below)
class BlogPostAdmin(SummernoteModelAdmin): # ... admin configuration for BlogPost ...

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
#admin.site.register(BlogPost) # no longer needed as decorator does this above
admin.site.register(BlogPostComments) #This registion allows users to create, comments on my blog posts.


from django.contrib import admin
from .models import BlogPost, BlogPostComments

# Register your models here.
admin.site.register(BlogPost) #This allows me to create, update and delete blog posts from the admin panel.
admin.site.register(BlogPostComments) 
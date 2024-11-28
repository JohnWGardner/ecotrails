from django.contrib import admin
from .models import BlogPost

# Register your models here.
admin.site.register(BlogPost) #This allows me to create, update and delete blog posts from the admin panel.
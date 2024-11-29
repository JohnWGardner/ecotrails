from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import BlogPost
# Create your views here.

class BlogPostList(generic.ListView): # Defines a class-based view for listing each blog post
    # model = BlogPost # This is made redundant by the queryset explicitly stating all posts are displayed.
    queryset = BlogPost.objects.filter(status=1) # Fetches all BlogPost objects from the database
    template_name = 'blog/blog_post_list.html' # optional addition for explicit naming, as i haven't followed blogpost_list default naming pattern


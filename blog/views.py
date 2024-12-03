from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import BlogPost
# Create your views here.

class BlogPostList(generic.ListView): # Defines a class-based view for listing each blog post
    # model = BlogPost # This is made redundant by the queryset explicitly stating all published (1) posts are displayed.
    queryset = BlogPost.objects.filter(status=1) # Fetches all BlogPost objects from the database
    template_name = "blog/index.html"
    paginate_by = 9
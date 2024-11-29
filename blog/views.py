from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import BlogPost
# Create your views here.

# class HomePage(TemplateView):
#     """
#     Displays home page
#     """
#     template_name = 'index.html'

class BlogPostList(generic.ListView):
    model = BlogPost
    template_name = 'blog/blog_post_list.html' # optional addition for explicit naming, as i haven't followed blogpost_list default naming pattern
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic
from .models import BlogPost
# Create your views here.

class BlogPostList(generic.ListView): # Defines a class-based view for listing each blog post
    # model = BlogPost # This is made redundant by the queryset explicitly stating all published (1) posts are displayed.
    queryset = BlogPost.objects.filter(status=1) # Fetches all BlogPost objects from the database
    template_name = "blog/index.html" #explicit naming of template name
    paginate_by = 6 # how many blogs are shown per page 

def post_detail(request, slug): #Display an individual :model:`blog.Post`. 
    #**Context** ``post`` An instance of :model:`blog.BlogPost`. **Template:** :template:`blog/post_detail.html`
    queryset = BlogPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )
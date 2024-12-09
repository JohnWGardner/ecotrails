from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import BlogPost, BlogPostComments
from .forms import CommentForm
# Create your views here.

class BlogPostList(generic.ListView): # Defines a class-based view for listing each blog post
    # model = BlogPost # This is made redundant by the queryset explicitly stating all published (1) posts are displayed.
    queryset = BlogPost.objects.filter(status=1) # Fetches all BlogPost objects from the database
    template_name = "blog/index.html" #explicit naming of template name
    paginate_by = 6 # how many blogs are shown per page 

def post_detail(request, slug): # Function to display the details of a blog post
    #**Context** ``post`` An instance of :model:`blog.BlogPost`. **Template:** :template:`blog/post_detail.html`
    queryset = BlogPost.objects.filter(status=1) # Fetch all published blog posts
    post = get_object_or_404(queryset, slug=slug) # Get the post by slug or return 404 if not found
    comments = post.blog_post_comments.all().order_by("-created_on") # Get all comments related to the post, ordered by creation date
    comment_count = post.blog_post_comments.filter(approved=True).count() # Count only approved comments

    comment_form = CommentForm() # Initialize comment_form here

    if request.method == "POST": # Check if the request method is POST
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST) # Bind data from POST request to the form
        if comment_form.is_valid(): # Check if the form data is valid
            comment = comment_form.save(commit=False) # Create a comment object without saving to the database yet
            comment.comment_author = request.user # Set the author of the comment to the current user
            comment.blogpost_id = post # Link the comment to the current post
            comment.save() # Save the comment to the database
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
            )
        comment_form = CommentForm() # Reinitialize form after saving comment
        
        print("About to render template")
    return render(
        request,
        "blog/post_detail.html", # Render the post_detail template
        {
            "post": post, # Pass the post object to the template
            "comments": comments, # Pass the comments to the template
            "comment_count": comment_count, # Pass the comment count to the template
            "comment_form": comment_form, # Pass the comment form to the template
        },
    )

def comment_edit(request, slug, comment_id): # This view function handles editing existing comments

    if request.method == "POST": # If the request is a POST (submitting the comment edit form)

        queryset = BlogPost.objects.filter(status=1) # Filter posts by published status (= 1)
        post = get_object_or_404(queryset, slug=slug) # Get the specific post based on its slug (URL identifier)
        comment = get_object_or_404(BlogPostComments, pk=comment_id) # Get the specific comment based on its primary key (comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment) # Initialize a CommentForm with submitted data and the existing comment object

        if comment_form.is_valid() and comment.comment_author == request.user: # Validate the form data and ensure the user owns the comment
            comment = comment_form.save(commit=False) # Save the form data to a comment object (but don't commit yet)
            comment.post = post  # Set the comment's associated post
            comment.approved = False # Set the comment's approval status to unapproved (needs moderation)
            comment.save() # Now save the updated comment object to the database
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!') # Add a success message for the user
        else:            # If form is invalid or user doesn't own the comment
            messages.add_message(request, messages.ERROR, 'Error updating comment!') # Add an error message for the user

    return HttpResponseRedirect(reverse('post_detail', args=[slug])) # Redirect the user back to the post detail page after editing the comment

def comment_delete(request, slug, comment_id):

# view to delete comment

    queryset = BlogPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(BlogPostComments, pk=comment_id)

    if comment.comment_author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
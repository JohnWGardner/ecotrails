from django.db import models #tools for defining database models, including fields, relationships, and querysets.
from django.contrib.auth.models import User # provides a user authentication system & features i.e. user permissions, login functionality.
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))  #Defines the possible statuses for a blog post: Draft or Published.


class BlogPost(models.Model): #from my ERD: Post Table. BlogPost class inherits properties and methods from the models.Model class
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True) #used to build a URL for each of our posts
    author_id = models.ForeignKey( # author_id is a foreign key referencing the primary key of the User
    User, on_delete=models.CASCADE, related_name="blog_posts" # CASCADE = on the deletion of the user entry, all their posts are also deleted.
    )
    content = models.TextField(default="") # This is the blog article content.
    created_on = models.DateTimeField(auto_now_add=True) #auto_now_add=True means the default created time is the time of post entry.
    status = models.IntegerField(choices=STATUS, default=0)  # Represents current status of blog post (Draft:0 (default) or Published:1).
    excerpt = models.TextField(blank=True) #creates a field that can store an excerpt - blank=True: indicates that the field is optional
    updated_on = models.DateTimeField(auto_now=True) #sets the value to the current date and time whenever the record is saved, not just when it is created.

    class Meta:
        ordering = ["created_on"] ## Order comments by creation date, newest first

    def __str__(self):
        return f"{self.title} | written by {self.author_id}"  # Returns a string representation of each BlogPost.title


class BlogPostComments(models.Model): #from my ERD: Post Table. BlogPostComments class inherits properties and methods from the models.Model class
    class Meta:
        verbose_name_plural = 'Blog Post Comments' #fixing plural metadata naming error without changing DB schema

    blogpost_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="blog_post_comments") #ForeignKey linking to BlogPost model; cascade delete to remove comments if the related blog post is deleted
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post_commenter") #ForeignKey linking to User model; cascade delete to remove comments if the related user is deleted
    body = models.TextField() # Field for the comment content
    approved = models.BooleanField(default=False) # Boolean indicating if the comment is approved; default is False
    created_on = models.DateTimeField(auto_now_add=True) # Timestamp for when the comment was created; auto-populated with the current date and time when the comment is created


# Use the model to update the database:
# After creating each model > convert the given Python class into instructions for the creation of the database table structure: python3 manage.py makemigrations blog
# Note: A blog/migrations/0001_initial.py file is created containing the instructions on what table to build

# Now we need to create that table in the database: python3 manage.py migrate blog
from django.db import models #tools for defining database models, including fields, relationships, and querysets.
from django.contrib.auth.models import User # provides a user authentication system & features i.e. user permissions, login functionality.
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))  #Defines the possible statuses for a blog post: Draft or Published.

class BlogPost(models.Model): #from my ERD: Post Table. BlogPost class inherits properties and methods from the models.Model class
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True) #used to build a URL for each of our posts
    author_id = models.ForeignKey( # author_id is a foreign key referencing the primary key of the User.id
    User, on_delete=models.CASCADE, related_name="blog_posts" # CASCADE = on the deletion of the user entry, all their posts are also deleted.
    )

content = models.TextField() # This is the blog article content.
created_on = models.DateTimeField(auto_now_add=True) #auto_now_add=True means the default created time is the time of post entry.
status = models.IntegerField(choices=STATUS, default=0)  # Represents current status of blog post (Draft:0 (default) or Published:1).





# Use the model to update the database
# After creating each model > convert the given Python class into instructions for the creation of the database table structure: python3 manage.py makemigrations blog
# Note: A blog/migrations/0001_initial.py file is created containing the instructions on what table to build

# Make migrations file for blog BlogPost model
# Now we need to create that table in the database

# python3 manage.py migrate blog


from django.db import models #tools for defining database models, including fields, relationships, and querysets.
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

# Use the model to update the database:
# After creating each model > convert the given Python class into instructions for the creation of the database table structure: python3 manage.py makemigrations blog
# Note: A blog/migrations/0001_initial.py file is created containing the instructions on what table to build

# Now we need to create that table in the database: python3 manage.py migrate blog
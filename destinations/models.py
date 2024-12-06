from django.db import models

# Create your models here.

class Destinations(models.Model):
    name = models.CharField(max_length=100, default='Unknown')
    description = models.TextField()   
    updated_on = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100, default='Unknown')
    
    def __str__(self):
        return self.name 

    class Meta: 
        verbose_name = "Destination" # Singular name
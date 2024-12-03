from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About) # This decorator registers the custom admin class for BlogPost, compared to the traditional approach of registering a model (as below)
class AboutAdmin(SummernoteModelAdmin): # ... admin configuration for BlogPost ...
    summernote_fields = ('content',)
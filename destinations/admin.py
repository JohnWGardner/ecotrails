from django.contrib import admin
from .models import Destination, Recommendation
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Destination)
class DestinationsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(Recommendation)
class RecommendationAdmin(SummernoteModelAdmin):
    
    list_display = ('place_name', 'user', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('place_name', 'description')
    date_hierarchy = 'created_on'
    ordering = ('approved', 'created_on')
from django.contrib import admin
from .models import Destinations
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Destinations)
class DestinationsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
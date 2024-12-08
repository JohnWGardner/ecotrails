from django.contrib import admin
from .models import Destination
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


admin.site.register(Destination)
class DestinationsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
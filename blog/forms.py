from .models import BlogPostComments
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogPostComments
        fields = ('body',)
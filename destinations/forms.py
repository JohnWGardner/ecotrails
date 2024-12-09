from django import forms
from .models import Recommendation

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['place_name', 'description']
from django.shortcuts import render
from .models import Destinations

# Create your views here.

def my_destinations(request):
    """
    Renders the About page
    """
    destinations = Destinations.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "destinations/destinations.html",
        {"destinations": destinations},
    )
from django.shortcuts import render
from .models import Contact
from .forms import CollaborateForm

# Create your views here.

def contact_me(request):
    """
    Renders the Contact page
    """
    contact = Contact.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "contact/contact.html",
        {"contact": contact, "collaborate_form": collaborate_form},
        
    )
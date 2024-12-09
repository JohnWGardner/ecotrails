from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Destination, Recommendation
from .forms import RecommendationForm

#

def destination_list(request):
    destinations = Destination.objects.filter(status=1).order_by('-created_on') # Fetch all published destinations, ordered by creation date
    destinations_by_continent = {} # This is a little different as I want to group destinations by continent.I'm having to set an empty dictionary to hold destinations grouped by continent
    for destination in destinations: # loop over each destination
        continent = destination.get_continent_display()  # set the display name to a varaible of the continent for the current destination
        if continent not in destinations_by_continent: #If the continent is not already a key in the dictionary, add it with an empty list
            destinations_by_continent[continent] = [] # add the current destination to the list of destinations for its continent
        destinations_by_continent[continent].append(destination)  # Fetch all approved recommendations
    recommendations = Recommendation.objects.filter(approved=True) 
    
    recommendation_form = RecommendationForm() # create a new empty recommendation form

    return render(
        request,
        "destinations/destination_list.html", # Render the destination_list template with the data
        {
            "destinations_by_continent": destinations_by_continent, # Pass grouped destinations to the template
            "recommendations": recommendations, # Pass approved recommendations to the template
            "recommendation_form": recommendation_form, # Pass the empty recommendation form to the template
        },
    )

def destination_detail(request, slug):
    queryset = Destination.objects.filter(status=1)  # Fetch all published destinations
    destination = get_object_or_404(queryset, slug=slug)  # Get the destination by slug or return 404 if not found
    recommendations = Recommendation.objects.filter(approved=True)  # Fetch all approved recommendations
    recommendation_form = RecommendationForm()  # Initialize an empty recommendation form
    if request.method == "POST":
        recommendation_form = RecommendationForm(data=request.POST)  # Bind data from POST request to the form
        if recommendation_form.is_valid():
            recommendation = recommendation_form.save(commit=False)  # Create a recommendation object without saving to the database yet
            recommendation.user = request.user  # Set the user of the recommendation to the current user
            recommendation.save()  # Save the recommendation to the database
            messages.add_message(
                request, messages.SUCCESS,
                'Recommendation submitted and awaiting approval'
            )  # Add a success message to be displayed to the user
            return HttpResponseRedirect(reverse('destination_detail', args=[slug]))  # Redirect to the same destination detail page
    return render(
        request,
        "destinations/destination_detail.html",
        {
            "destination": destination,  # Pass the destination object to the template
            "recommendations": recommendations,  # Pass approved recommendations to the template
            "recommendation_form": recommendation_form,  # Pass the recommendation form to the template
        },
    )
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Destination, Recommendation
from .forms import RecommendationForm

def destination_list(request):
    destinations = Destination.objects.filter(status=1).order_by('-created_on')  # Fetch all published destinations, ordered by creation date
    destinations_by_continent = {}  # This is a little different as I want to group destinations by continent.I'm having to set an empty dictionary to hold destinations grouped by continent
    for destination in destinations:  # Loop over each destination
        continent = destination.get_continent_display()  # Get the display name of the continent for the current destination
        if continent not in destinations_by_continent:  # If the continent is not already a key in the dictionary, add it with an empty list
            destinations_by_continent[continent] = []  # add an empty list for the continent
        destinations_by_continent[continent].append(destination)  # add the current destination to the list for its continent
    
    recommendations = Recommendation.objects.filter(approved=True)  # create a new empty recommendation form

    if request.method == "POST":  # Check if the request method is POST
        recommendation_form = RecommendationForm(data=request.POST)  # pass data from POST request to the form
        if recommendation_form.is_valid():  # Check if the form is valid
            recommendation = recommendation_form.save(commit=False)  # Create a recommendation ref without saving to the database yet
            recommendation.user = request.user  # Set the user of the recommendation to the current user
            recommendation.save()  # Save the recommendation to the database
            messages.add_message(
                request, messages.SUCCESS,
                'Recommendation submitted and awaiting approval'
            )  # Add a success message to be displayed to the user
            return HttpResponseRedirect(reverse('destination_list'))  # Redirect to the destination list page
    else:
        recommendation_form = RecommendationForm()  # create a new empty recommendation form

    return render(
        request,
        "destinations/destination_list.html",  # render the destination_list template with the data
        {
            "destinations_by_continent": destinations_by_continent,  # pass grouped destinations to the template
            "recommendations": recommendations,  # pass approved recommendations to the template
            "recommendation_form": recommendation_form,  # pass the recommendation form to the template
        },
    )

def destination_detail(request, slug):
    queryset = Destination.objects.filter(status=1)  # get all published destinations
    destination = get_object_or_404(queryset, slug=slug)  # get the destination by slug or return 404 if not found
    recommendations = Recommendation.objects.filter(approved=True)  # get all approved recommendations
    recommendation_form = RecommendationForm()  # add an empty recommendation form
    if request.method == "POST":
        recommendation_form = RecommendationForm(data=request.POST)  # get data from POST request to the form
        if recommendation_form.is_valid():
            recommendation = recommendation_form.save(commit=False)  # create a recommendation object without saving to the database yet
            recommendation.user = request.user  # set the user of the recommendation to the current user
            recommendation.save()  # save the recommendation to the database
            messages.add_message(
                request, messages.SUCCESS,
                'Recommendation submitted and awaiting approval'
            )  # add a success message to be displayed to the user
            return HttpResponseRedirect(reverse('destination_detail', args=[slug]))  # redirect to the same destination detail page
    return render(
        request,
        "destinations/destination_detail.html",
        {
            "destination": destination,  # pass the destination object to the template
            "recommendations": recommendations,  # pass approved recommendations to the template
            "recommendation_form": recommendation_form,  # pass the recommendation form to the template
        },
    )

def recommendation_edit(request, slug, recommendation_id):
    if request.method == "POST":
        queryset = Destination.objects.filter(status=1)
        destination = get_object_or_404(queryset, slug=slug)
        recommendation = get_object_or_404(Recommendation, pk=recommendation_id)
        recommendation_form = RecommendationForm(data=request.POST, instance=recommendation)

        if recommendation_form.is_valid() and recommendation.user == request.user:
            recommendation = recommendation_form.save(commit=False)
            recommendation.destination = destination
            recommendation.approved = False
            recommendation.save()
            messages.add_message(request, messages.SUCCESS, 'Recommendation Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating recommendation!')

    return render(
        request,
        "destinations/recommendation_edit.html",
        {
            "form": recommendation_form,
        },
    )

def recommendation_delete(request, slug, recommendation_id):
    recommendation = get_object_or_404(Recommendation, pk=recommendation_id)
    if request.method == "POST":
        recommendation.delete()
        messages.add_message(request, messages.SUCCESS, 'Recommendation deleted successfully')
        return redirect('destination_detail', slug=slug)

    return render(
        request,
        "destinations/recommendation_delete.html",
        {
            "recommendation": recommendation,
        },
    )
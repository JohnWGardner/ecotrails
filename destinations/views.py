from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Destination

class DestinationList(generic.ListView):
    queryset = Destination.objects.filter(status=1).order_by('-created_on')
    template_name = "destinations/destination_list.html"
    paginate_by = 6

def destination_detail(request, slug):
    queryset = Destination.objects.filter(status=1)
    destination = get_object_or_404(queryset, slug=slug)
    return render(
        request,
        "destinations/destination_detail.html",
        {
            "destination": destination,
        },
    )
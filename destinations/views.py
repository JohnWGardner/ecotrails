from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Destination

class DestinationList(generic.ListView):
    queryset = Destination.objects.filter(status=1).order_by('-created_on')
    template_name = "destinations/destination_list.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            destinations_by_continent = {}
            for destination in self.get_queryset():
                continent = destination.get_continent_display()
                if continent not in destinations_by_continent:
                    destinations_by_continent[continent] = []
                destinations_by_continent[continent].append(destination)
            context['destinations_by_continent'] = destinations_by_continent
            return context

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
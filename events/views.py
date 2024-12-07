from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Event
# Create your views here.
from django.shortcuts import render,HttpResponse


def events(request):
    return render(request, 'events.html')

def event_detail(request, slug):
    # Logic to fetch the event details using the slug
    # For example:
    event = get_object_or_404(EventModel, slug=slug)  # Replace EventModel with your actual model
    return render(request, 'event_detail.html', {'event': event})



def event_detail(request, event_slug):
    event = get_object_or_404(Event, slug=event_slug)
    return render(request, 'event_detail.html', {'event': event})

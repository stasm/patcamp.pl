from django.shortcuts import render, get_object_or_404

from talks.models import Speaker, Venue, Event, Talk

def home(request):
    events = Event.objects.all()
    return render(request, "talks/home.html",
                  {'events': events})

def event(request, event_id):
    e = get_object_or_404(Event, pk=event_id)
    return render(request, "talks/home.html")

def speaker(request):
    pass

def talk(request):
    pass

def venue(request):
    pass

from django.shortcuts import render, get_object_or_404

from talks.models import Speaker, Venue, Event, Talk

def home(request):
    upcoming = []
    past = []
    for e in Event.objects.all():
        print e.day
        print e.time
        if e.upcoming():
            upcoming.append(e)
        else:
            past.append(e)
    return render(request, "talks/home.html", {
        'upcoming': upcoming,
        'past': past,
        })

def event(request, event_id):
    e = get_object_or_404(Event, pk=event_id)
    return render(request, "talks/home.html")

def speaker(request, speaker_id):
    pass

def talk(request, talk_id):
    pass

def venue(request, venue_id):
    pass

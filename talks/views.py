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
    width = 640 * len(upcoming) + 455 * len(past)
    return render(request, "talks/home.html", {
        'upcoming': upcoming,
        'past': past,
        'width': width,
    })

def event(request, event_id):
    e = get_object_or_404(Event, pk=event_id)
    return render(request, "talks/event.html", {
        'event': e,
    })

def speaker(request, speaker_id, speaker_slug):
    s = get_object_or_404(Speaker, pk=speaker_id)
    return render(request, "talks/speaker.html", {
        'speaker': s,
    })

def talk(request, talk_id, talk_slug):
    t = get_object_or_404(Talk, pk=talk_id)
    return render(request, "talks/talk.html", {
        'talk': t,
    })

def venue(request, venue_id):
    v = get_object_or_404(Venue, pk=venue_id)
    return render(request, "talks/venue.html", {
        'venue': v,
    })

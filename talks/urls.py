from django.conf.urls import patterns, url

urlpatterns = patterns('talks.views',
    url(r'^$', 'home', name='home'),
    url(r'^e/(?P<event_id>\d+)', 'event', name='event'),
    url(r'^o/(?P<speaker_id>\d+)/(?P<speaker_slug>.+)', 'speaker',
        name='speaker'),
    url(r'^p/(?P<talk_id>\d+)/(?P<talk_slug>.+)', 'talk', name='talk'),
    url(r'^m/(?P<venue_id>\d+)', 'venue', name='venue'),
)

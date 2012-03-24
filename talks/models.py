import datetime

from django.db import models
from django.utils.safestring import mark_safe

class Speaker(models.Model):
    name = models.CharField(max_length=80)
    sort_name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    bio = models.TextField()
    pic = models.ImageField(upload_to="speakers/", blank=True)

    class Meta:
        ordering = ("sort_name",)
        verbose_name = "spiker"
        verbose_name_plural = "spikerzy"

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('talks.views.speaker', (), { 
            'speaker_id': self.id,
            'speaker_slug': self.slug,
        })


class Venue(models.Model):
    name = models.CharField(max_length=80)
    address = models.TextField(blank=True)
    description = models.TextField(blank=True)
    maps_url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "miejsce"
        verbose_name_plural = "miejsca"

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('talks.views.venue', (), { 'venue_id': self.id })


class Event(models.Model):
    date = models.DateTimeField()
    summary = models.TextField(blank=True)
    location = models.ForeignKey(Venue)
    fb = models.CharField(max_length=20)
    yt = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ("-date",)
        verbose_name = "spotkanie"
        verbose_name_plural = "spotkania"

    def __unicode__(self):
        return str(self.date.date())

    @models.permalink
    def get_absolute_url(self):
        return ('talks.views.event', (), { 'event_id': self.id })

    @property
    def facebook(self):
        return "https://www.facebook.com/events/%s/" % self.fb

    @property
    def youtube(self):
        return "http://www.youtube.com/playlist?list=%s" % self.yt

    @property
    def day(self):
        return self.date.date().strftime("%d %B")

    @property
    def time(self):
        return self.date.strftime("%H:%M")

    def upcoming(self):
        event_day = self.date.date()
        today = datetime.date.today()
        if today < event_day:
            return "upcoming"
        elif today == event_day:
            return "today"
        else:
            return False

    def processed(self):
        return bool(self.yt)


class Talk(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    summary = models.TextField(blank=True)
    slug = models.SlugField(max_length=200)
    yt = models.CharField(max_length=20, blank=True)
    speakers = models.ManyToManyField(Speaker)
    event = models.ForeignKey(Event, related_name="talks")
    pic = models.ImageField(upload_to="talks/", blank=True)

    class Meta:
        verbose_name = "prezentacja"
        verbose_name_plural = "prezentacje"

    def __unicode__(self):
        speakers = [unicode(spk) for spk in self.speakers.all()]
        return "%s (%s)" % (self.title, ", ".join(speakers))

    @models.permalink
    def get_absolute_url(self):
        return ('talks.views.talk', (), { 
            'talk_id': self.id,
            'talk_slug': self.slug,
        })

    @property
    def youtube(self):
        return "http://youtu.be/%s" % self.yt

    @property
    def youtube_playlist(self):
        return "http://youtu.be/%s?list=%s" % (self.yt, self.event.yt)

    def youtube_embed(self):
        return mark_safe("""
            <iframe width="560" height="315"
              src="http://www.youtube.com/embed/%s" 
              frameborder="0" allowfullscreen></iframe>
        """ % self.yt)

    def facebook_comments(self):
        return mark_safe("""
            <div class="fb-comments"
              data-href="http://patcamp.pl%s"
              data-num-posts="2" 
              data-width="560"></div>
        """ % self.get_absolute_url())

    def facebook_like(self):
        return mark_safe("""
            <div class="fb-like" 
              data-href="http://patcamp.pl%s"
              data-send="false"
              data-width="560"
              data-show-faces="true"></div>
        """ % self.get_absolute_url())


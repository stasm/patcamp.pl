from talks.models import Speaker, Venue, Event, Talk
from django.contrib import admin

class SpeakerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class TalkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Talk, TalkAdmin)

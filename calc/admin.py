from django.contrib import admin
from .models import Calendar,Participant,Event

# Register your models here.


admin.site.register(Calendar)
admin.site.register(Participant)
admin.site.register(Event)


from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Calendar, Event
from .serializers import(CalendarSerializer,
						EventSerializer
)


class CalendarViewSet(ModelViewSet):
	queryset=Calendar.objects.all()
	serializer_class=CalendarSerializer

class EventViewSet(ModelViewSet):
	queryset=Event.objects.all()
	serializer_class=EventSerializer

	search_fields = ['title']
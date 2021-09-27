from rest_framework import serializers
from .models import Calendar,Participant,Event
from drf_writable_nested.serializers import WritableNestedModelSerializer

class ParticipantSerializer(serializers.ModelSerializer):
	class Meta:
		model=Participant
		fields=['id','email']

class EventSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
	participants = ParticipantSerializer(many=True)

	class Meta:
		model=Event
		fields=['id','title','description','start_date','end_date','color', 'calendar', 'participants']

	def create(self,validated_data):
		participants=validated_data.pop('participants')
		event=Event.objects.create(**validated_data)
		for participant in participants:
			Participant.objects.create(event=event,**participant)
		return event


class CalendarSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
	events=EventSerializer(many=True)
	class Meta:
		model=Calendar
		fields=['id','name','description','events']


	def create(self,validated_data):
		events=validated_data.pop('events')
		calendar=Calendar.objects.create(**validated_data)
		for event in events:
			Event.objects.create(calendar=calendar,**event)
		return calendar





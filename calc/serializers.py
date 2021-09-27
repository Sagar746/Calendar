from rest_framework import serializers
from .models import Calendar,Participant,Event
from drf_writable_nested.serializers import WritableNestedModelSerializer


class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model=Event
		fields=['id','title','description','start_date','end_date','color']


class CalendarSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
	events=EventSerializer(many=True)
	class Meta:
		model=Calendar
		fields=['id','calendar_name','description','events']


	def create(self,validated_data):
		events=validated_data.pop('events')
		calendar=Calendar.objects.create(**validated_data)
		for event in events:
			Event.objects.create(calendar=calendar,**event)
		return calendars


class ParticipantSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
	events=EventSerializer(many=True)
	class Meta:
		model=Participant
		fields=['id','email','events']

	def create(self,validated_data):
		events=validated_data.pop('events')
		participants=Participant.objects.create(**validated_data)
		for event in events:
			Event.objects.create(participants=participants,**event)
		return participants




from rest_framework import serializers
from .models import Calendar,Event
from drf_writable_nested.serializers import WritableNestedModelSerializer

class EventSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

	class Meta:
		model=Event
		fields=['id','title','description','start','end','color', 'calendar', 'participants']

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





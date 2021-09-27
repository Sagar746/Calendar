from django.urls import path,include
from .views import(CalendarViewSet,
				   ParticipantViewSet,
				   EventViewSet
)

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('calendar', CalendarViewSet, basename='calendar')
router.register('participant', ParticipantViewSet, basename='participant')
router.register('event', EventViewSet, basename='event')


urlpatterns=[
	path('api/',include(router.urls)),
]
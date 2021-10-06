from django.urls import path,include
from .views import(CalendarViewSet,
				   EventViewSet
)

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('calendar', CalendarViewSet, basename='calendar')
router.register('event', EventViewSet, basename='event')


urlpatterns=[
	path('api/',include(router.urls)),
]
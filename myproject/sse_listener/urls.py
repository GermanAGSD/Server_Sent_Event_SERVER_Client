from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.dashboard, name="events_dashboard"),
    path("events/api/", views.events_api, name="events_api"),
]

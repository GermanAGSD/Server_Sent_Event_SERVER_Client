# player/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.video_player, name="video_player"),
]

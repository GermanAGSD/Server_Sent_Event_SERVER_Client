from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def video_player(request):
    return render(request, "player.html")

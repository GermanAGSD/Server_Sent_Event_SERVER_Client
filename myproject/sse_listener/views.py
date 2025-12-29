from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import SseEvent
from django.http import JsonResponse
from .models import SseEvent

def dashboard(request):
    events = SseEvent.objects.order_by("-received_at")[:20]
    return render(request, "sse_listener/dashboard.html", {"events": events})


def events_api(request):
    """Возвращает последние события в JSON"""
    events = list(
        SseEvent.objects.order_by("-received_at")
        .values("event_type", "content", "received_at")[:20]
    )
    return JsonResponse(events, safe=False)

from django.contrib import admin

# Register your models here.
# sse_listener/admin.py
from django.contrib import admin
from .models import SseEvent

@admin.register(SseEvent)
class SseEventAdmin(admin.ModelAdmin):
    list_display = ("event_type", "received_at")
    ordering = ("-received_at",)

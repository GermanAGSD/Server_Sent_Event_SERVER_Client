from django.db import models

class SseEvent(models.Model):
    event_type = models.CharField(max_length=50)
    content = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} @ {self.received_at:%H:%M:%S}"

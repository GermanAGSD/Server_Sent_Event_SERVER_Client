from django.apps import AppConfig
import threading
import asyncio

class SseListenerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sse_listener"

    def ready(self):
        """Запуск клиента при старте Django"""
        from .sse_client import DjangoSSEClient

        def start_client():
            asyncio.run(DjangoSSEClient().run())

        thread = threading.Thread(target=start_client, daemon=True)
        thread.start()
        print("🚀 SSE-клиент запущен в фоновом потоке")

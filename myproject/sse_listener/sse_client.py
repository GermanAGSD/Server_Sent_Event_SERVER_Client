import asyncio
import aiohttp
import json
from asgiref.sync import sync_to_async
from django.utils import timezone
from django.db import transaction
from .models import SseEvent


FASTAPI_SSE_URL = "http://192.168.19.13:8000/sse/host?param=DJANGO"


class DjangoSSEClient:
    """Асинхронный клиент для получения SSE событий от FastAPI"""
    def __init__(self, url=FASTAPI_SSE_URL, reconnect_delay=3):
        self.url = url
        self.reconnect_delay = reconnect_delay
        self._running = False

    async def run(self):
        self._running = True
        print(f"🔌 Connecting to {self.url} ...")

        while self._running:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(self.url, timeout=None) as resp:
                        if resp.status != 200:
                            print(f"⚠️ Connection failed: HTTP {resp.status}")
                            await asyncio.sleep(self.reconnect_delay)
                            continue

                        print("✅ Connected to FastAPI SSE")
                        async for line in resp.content:
                            line = line.decode("utf-8").strip()
                            if not line.startswith("data:"):
                                continue

                            data = line[5:].strip()
                            try:
                                payload = json.loads(data)
                            except json.JSONDecodeError:
                                payload = {"text": data}

                            await self.save_event(payload)

            except Exception as e:
                print(f"💥 SSE client error: {e}")
                await asyncio.sleep(self.reconnect_delay)

    @sync_to_async
    @transaction.atomic
    def save_event(self, payload):
        """Сохраняет событие в базу"""
        SseEvent.objects.create(
            event_type=payload.get("event", "unknown"),
            content=json.dumps(payload),
            received_at=timezone.now()
        )
        print(f"📨 Event saved: {payload}")

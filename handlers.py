import asyncio
from typing import Protocol, runtime_checkable
from .task import Task

@runtime_checkable
class TaskHandler(Protocol):
    async def handle(self, task: Task) -> None:
        ...

class DefaultHandler(TaskHandler):
    async def handle(self, task: Task) -> None:
        print(f"[Обработчик] Взялся за задачу {task.id}...")

        await asyncio.sleep(1)

        task.status = "sent"
        print(f"[Обработчик] УСПЕХ: Задача {task.id} выполнена. Статус: {task.status}")


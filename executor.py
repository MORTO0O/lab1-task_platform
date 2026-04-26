import asyncio
from typing import Dict, Type
from .task import Task
from .handlers import TaskHandler
from .exceptions import TaskError

class AsyncExecutor:
    def __init__(self):
        self._queue = asyncio.Queue()
        self._handlers: Dict[str, Type[TaskHandler]] = {}
        self._worker_task = None

    def register_handler(self, handler_name: str, handler: TaskHandler):
        self._handlers[handler_name] = handler

    async def add_task(self, task: Task):
        await self._queue.put(task)
        print(f"[Очередь] Задача {task.id} добавлена в очередь")

    async def _worker(self):
        while True:
            task: Task = await self._queue.get()

            try:
                handler = self._handlers.get("default")
                if not handler:
                    raise Exception("Нет доступного обработчика.")

                await handler.handle(task)


            except TaskError as e:
                print(f"[ОШИБКА БИЗНЕС-ЛОГИКИ] Ошибка в задаче {task.id}: {e}")
            except Exception as e:
                print(f"[КРИТИЧЕСКАЯ ОШИБКА] Сбой при обработке {task.id}: {e}")
            finally:
                self._queue.task_done()

    async def __aenter__(self):
        print("\n[Executor] Запуск системы...")
        self._worker_task = asyncio.create_task(self._worker())
        return self

    async def __aexit__(self, exc_type, exc_val, exc_t):
        print("\n[Executor] Инициирована остановка. Ожидание завершения текущих задач...")
        await self._queue.join()
        self._worker_task.cancel()
        print("[Executor] Система остановлена без рисков.")

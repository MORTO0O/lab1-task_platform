from .receiver import TaskReceiver
from .sources.file_source import FileTaskSource
from .sources.generator_source import GeneratorTaskSource
from .sources.API_source import APITaskSource
from .exceptions import TaskError
from .queue import TaskQueue
import asyncio
from src.executor import AsyncExecutor
from src.handlers import DefaultHandler

if __name__ == '__main__':
    receiver = TaskReceiver()

    receiver.add_source(FileTaskSource("src/tasks.json"))
    receiver.add_source(GeneratorTaskSource(count=8))
    receiver.add_source(APITaskSource())

    queue = TaskQueue()

    print("\nЗагрузка задач в очередь...")
    queue.add_tasks(receiver.stream_tasks())

    print('\n<<<<< Все задачи >>>>>')
    for task in queue:
        print(f"[{task.id}] Приоритет: {task.priority}, Статус: {task.status}")

    print("<<<<< Фильтрация от приоритета 4+ >>>>>")
    high_priority = queue.filter_by_priority(4)
    for task in high_priority:
        print(f"ВАЖНАЯ ЗАДАЧА: {task.id} Приоритет: {task.priority}")




    all_tasks_list = list(queue)
    print(f"\nВсего задач в очереди: {len(all_tasks_list)}")

    async def run_async_system():
        async with AsyncExecutor() as executor:
            executor.register_handler("default", DefaultHandler())

            print("Постановка задач в очередь...")
            tasks_to_run = list(queue)[:5]

            for task in tasks_to_run:
                await executor.add_task(task)

    asyncio.run(run_async_system())
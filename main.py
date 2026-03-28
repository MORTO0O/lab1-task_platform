from .receiver import TaskReceiver
from .sources.file_source import FileTaskSource
from .sources.generator_source import GeneratorTaskSource
from .sources.API_source import APITaskSource
from .exceptions import TaskError

if __name__ == '__main__':
    receiver = TaskReceiver()

    receiver.add_source(FileTaskSource("src/tasks.json"))
    receiver.add_source(GeneratorTaskSource(count=8))
    receiver.add_source(APITaskSource())

    print("Collecting tasks from all sources...\n")

    tasks_stream = iter(receiver.stream_tasks())

    while True:
        try:
            task = next(tasks_stream)
            _ = task.access_log

            print(f"OK: [ID: {task.id}] | Priority: {task.priority} | Status: {task.status}")

            if task.is_high_priority:
                print(f"Внимание! Высокий приоритет у задачи {task.id}")

        except StopIteration:
            break
        except TaskError as e:
            print(f"\n[ОШИБКА ВАЛИДАЦИИ]: {e}")
        except Exception as e:
            print(f"\n[НЕПРЕДВИДЕННАЯ ОШИБКА]: {e}")
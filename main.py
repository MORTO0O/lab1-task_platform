from .receiver import TaskReceiver
from .sources.file_source import FileTaskSource
from .sources.generator_source import GeneratorTaskSource
from .sources.API_source import APITaskSource

if __name__ == '__main__':
    receiver = TaskReceiver()

    receiver.add_source(FileTaskSource("data/tasks.json"))
    receiver.add_source(GeneratorTaskSource(count=5))
    receiver.add_source(APITaskSource())

    print("Collecting tasks from all sources...\n")

    for task in receiver.stream_tasks():
        print(f"done: Task {task.id} | payload {task.payload}")

    print(f"\nNumber of tasks: {len(receiver.collect_tasks())}")
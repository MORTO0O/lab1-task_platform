from typing import Iterable

from ..task import Task

class GeneratorTaskSource:
    def __init__(self, count: int = 10) -> None:
        self.count = count

    def get_tasks(self) -> Iterable[Task]:
        for i in range(self.count):
            yield Task(id=f"gen_{i:04d}",
                       payload={"type": "generated", "value": i * 10}
            )

from typing import Iterable

from ..task import Task

class APITaskSource:
    def get_tasks(self) -> Iterable[Task]:
        yield Task(id="api001", payload={...})
        yield Task(id="api002", payload={...})
        yield Task(id="api003", payload={...})

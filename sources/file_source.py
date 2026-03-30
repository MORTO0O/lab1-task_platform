import json
from pathlib import Path
from typing import Iterable
from ..task import Task

class FileTaskSource:
    def __init__(self, filepath: str | Path):
        self.filepath = Path(filepath)

    def get_tasks(self) -> Iterable[Task]:
        if not self.filepath.exists():
            return
        with open(self.filepath, encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            yield Task(
                task_id=str(item.get('task_id', item.get('id'))),
                payload=item.get('payload', {}),
                priority=int(item.get('priority', 1)),
                description=item.get('description', 'No description provided')
            )
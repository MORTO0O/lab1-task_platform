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
                id=str(item['id']),
                payload=item.get('payload', {})
            )
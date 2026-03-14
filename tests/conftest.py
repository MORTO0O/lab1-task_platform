import json
import tempfile
from pathlib import Path

import pytest

from src.task import Task


@pytest.fixture
def sample_tasks_data():
    return [
        {"id": "file_001", "payload": {"type": "test", "value": 100}},
        {"id": "file_002", "payload": {"type": "test", "value": 200}},
        {"id": "file_003", "payload": {"message": "hello"}},
    ]


@pytest.fixture
def temp_task_file(sample_tasks_data):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(sample_tasks_data, f, ensure_ascii=False, indent=2)
        temp_path = Path(f.name)

    yield temp_path

    if temp_path.exists():
        temp_path.unlink()
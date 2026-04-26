import pytest
import types
from src.task import Task
from src.queue import TaskQueue

def test_add_and_iterate():
    q = TaskQueue()
    t1 = Task(task_id=1, description="Задача 1", payload={}, priority=1, status="ready")
    t2 = Task(task_id=2, description="Задача 2", payload={}, priority=5, status="sent")

    q.add_task(t1)
    q.add_task(t2)

    tasks_list = list(q)

    assert len(tasks_list) == 2
    assert tasks_list[0].id == 1

def test_repeated_iteration():
    q = TaskQueue()
    q.add_task(Task(task_id=1, description="Тест", payload={}, priority=1, status="ready"))

    # Обходим очередь первый раз
    first_pass = list(q)
    # Обходим очередь второй раз
    second_pass = list(q)

    # Если бы __iter__ был написан неправильно, второй список был бы пустым!
    assert len(first_pass) == 1
    assert len(second_pass) == 1


# 3. Тест на ленивый фильтр (Генератор)
def test_filter_by_status():
    q = TaskQueue()
    q.add_task(Task(task_id=1, description="A", payload={}, priority=1, status="ready"))
    q.add_task(Task(task_id=2, description="B", payload={}, priority=5, status="sent"))
    q.add_task(Task(task_id=3, description="C", payload={}, priority=3, status="ready"))

    # Вызываем метод
    generator = q.filter_by_status("ready")

    # ФИШКА ДЛЯ ЗАЩИТЫ: Проверяем, что метод вернул именно ГЕНЕРАТОР, а не обычный список!
    assert isinstance(generator, types.GeneratorType)

    # Теперь "выкачиваем" данные из генератора
    ready_tasks = list(generator)

    assert len(ready_tasks) == 2
    assert ready_tasks[0].id == 1
    assert ready_tasks[1].id == 3


def test_filter_by_priority():
    q = TaskQueue()
    q.add_task(Task(task_id=1, description="A", payload={}, priority=1, status="ready"))
    q.add_task(Task(task_id=2, description="B", payload={}, priority=5, status="sent"))
    q.add_task(Task(task_id=3, description="C", payload={}, priority=4, status="ready"))

    high_priority = list(q.filter_by_priority(4))

    assert len(high_priority) == 2
    assert high_priority[0].id == 2
    assert high_priority[1].id == 3

def test_sum_compatibility():
    q = TaskQueue()
    q.add_task(Task(task_id=1, description="A", payload={}, priority=2, status="ready"))
    q.add_task(Task(task_id=2, description="B", payload={}, priority=3, status="ready"))

    total_priority = sum(task.priority for task in q)

    assert total_priority == 5

    q.add_task(Task(task_id=3, description="C", payload={}, priority=5, status="ready"))

    high_priority_count = sum(1 for task in q if task.is_high_priority)
    assert high_priority_count == 1
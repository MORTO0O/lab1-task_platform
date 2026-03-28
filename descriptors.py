from .exceptions import InvalidPriorityError
from .task import TaskSource


class PriorityDescriptor:
    def __init__(self, min_priority: int = 1, max_priority: int = 5):
        self.min_priority = min_priority
        self.max_priority = max_priority

    def __set_name__(self, owner, name: str):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.__class__):
            raise InvalidPriorityError(f"Приоритет должен быть числом")

        if not (self.min_priority <= value <= self.max_priority):
            raise InvalidPriorityError(
                f"Приоритет должен быть от {self.min_priority} до {self.max_priority}"
            )

        instance.__dict__[self.name] = value

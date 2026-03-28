class TaskError(Exception):
    pass
class InvalidPriorityError(TaskError):
    pass
class InvalidStatusError(TaskError):
    pass
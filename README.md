# Лабораторная работа №1  
**Источники задач и контракты**

**Тема:** Duck Typing, `typing.Protocol` и контрактное программирование

## Цель работы
Освоить структурную типизацию через `Protocol`, реализовать runtime-проверку контракта и создать расширяемую подсистему приёма задач **без общего базового класса**.

## Реализованные возможности
- Единый контракт `TaskSource` с помощью `typing.Protocol`
- `@runtime_checkable` + проверка через `isinstance()`
- Три независимых источника задач:
  - `FileTaskSource` - загрузка из JSON
  - `GeneratorTaskSource` - генерация задач в коде
  - `APITaskSource` - заглушка внешнего API
- Ленивая обработка задач (`yield from`)
- Полная типизация и 91% покрытие тестами

## Структура проекта

```
task_platform/
├── task.py                    # Модель Task + протокол TaskSource
├── receiver.py                # TaskReceiver + runtime-проверка
├── sources/
│   ├── file_source.py
│   ├── generator_source.py
│   └── API_source.py
├── main.py                    # Демонстрация работы
├── tests/                     # Все тесты (pytest)
├── tasks.json                 # Пример данных
├── .gitignore
├── requirements.txt
├── .pre-commit-config.yaml
└── README.md
```

## Как запустить

```powershell
# 1. Переход в родительскую директорию
cd C:\Users\Пользователь\PycharmProjects\frameworks

# 2. Запуск демонстрации
python -m task_platform.main

# 3. Запуск тестов с покрытием
python -m pytest task_platform/tests -q --cov=task_platform --cov-report=term-missing
```
## Чему научился
- Использовать современный `Protocol` вместо ABC
- Проводить runtime-проверку контрактов (`@runtime_checkable`)
- Строить расширяемую архитектуру (Open-Closed Principle)
- Писать ленивые генераторы и качественные тесты на **pytest** (91% покрытие)
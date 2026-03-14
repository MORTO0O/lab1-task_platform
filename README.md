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
src/
├── task.py                    # Модель Task + протокол TaskSource
├── receiver.py                # TaskReceiver с runtime-проверкой
├── sources/
│   ├── file_source.py
│   ├── generator_source.py
│   └── API_source.py
├── main.py                    # Демонстрация
├── tests/                     # Тесты на pytest
├── tasks.json
├── descriptors.py             # ← будет добавлен во 2-й лабе
├── exceptions.py              # ← будет добавлен во 2-й лабе
├── .gitignore
├── requirements.txt
└── .pre-commit-config.yaml
```

## Как запустить (независимо от названия папки)

```powershell
# Запуск демонстрации
python -m src.main

# Запуск тестов с покрытием
python -m pytest src/tests -q --cov=src --cov-report=term-missing
```
## Чему научился
- Использовать современный `Protocol` вместо ABC
- Проводить runtime-проверку контрактов (`@runtime_checkable`)
- Строить расширяемую архитектуру (Open-Closed Principle)
- Писать ленивые генераторы и качественные тесты на **pytest** (91% покрытие)
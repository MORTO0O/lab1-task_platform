# Лабораторная работа №1: Источники задач и контракты

**Вариант с полным использованием `typing.Protocol` + `@runtime_checkable`**

## Тема
Duck Typing, протоколы и контрактное программирование в Python

## Цель работы
Освоить структурную типизацию через `Protocol`, реализовать runtime-проверку контрактов, создать расширяемую архитектуру без общего базового класса.

## Что реализовано
- Единый поведенческий контракт `TaskSource` (без наследования)
- `@runtime_checkable` + `isinstance()` проверка
- Три независимых источника задач:
  - `FileTaskSource` (из JSON)
  - `GeneratorTaskSource` (программная генерация)
  - `APITaskSource` (заглушка внешнего API)
- Ленивая обработка через генераторы (`yield from`)
- Полная типизация + 91% покрытие тестами

## Установка
```powershell
# 1. Клонируем
git clone https://github.com/MORTO0O/lab1-task_platform.git
cd task-platform-lab1

# 2. Создаём окружение
python -m venv .venv
.venv\Scripts\activate     # Windows

# 3. Устанавливаем зависимости
pip install -r requirements.txt

# 4. (Опционально) включаем pre-commit
pre-commit install
```
## Запуск
```powershell
# Демонстрация
python -m main

# Тесты
python -m pytest tests -q --cov=. --cov-report=term-missing
```
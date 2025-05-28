'''
Напишіть функцію divide_numbers, яка приймає два аргументи та ділить перше число на друге.
Якщо виникає виключення ZeroDivisionError, перехопіть його і виведіть стек-трейс,
використовуючи модуль traceback.
Вимоги:
•	Програма повинна імпортувати модуль traceback для використання його функціональності.
•	Програма повинна включати функцію divide_numbers, яка приймає два аргументи.
•	Функція divide_numbers повинна виконувати ділення першого аргументу на другий і
перехоплювати виключення ZeroDivisionError.
•	Якщо виникає виключення ZeroDivisionError, функція divide_numbers повинна
виводити стек-трейс з використанням модуля traceback.
'''
import traceback

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Помилка: ділення на нуль!")
        traceback.print_exc()
print(divide_numbers(10, 2))   # Вивід: 5.0
print(divide_numbers(5, 0))    # Вивід: Помилка + стек-трейс
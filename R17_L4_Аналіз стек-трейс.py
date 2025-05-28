'''
Напишіть функцію complex_operation,
яка викликає декілька вкладених функцій і може викликати виключення. Якщо виникає виключення,
перехопіть його і витягніть "сирі" відомості про трасування стека з використанням
 traceback.extract_tb(). Виведіть інформацію про кожен фрейм стека
 (файл, рядок, ім'я функції, текст рядка).
Вимоги:
•	Програма повинна включати функцію complex_operation, яка викликає декілька вкладених функцій
 і може викликати виключення.
•	Функція complex_operation повинна перехоплювати виниклі виключення за допомогою конструкції
 try-except.
•	При виникненні виключення, функція complex_operation повинна використовувати
traceback.extract_tb() для витягнення "сирих" відомостей про трасування стека.
•	Функція complex_operation повинна виводити файл, рядок, ім'я функції і
текст рядка для кожного фрейму стека.
'''
import traceback

def inner_function():
    # Спроба викликати виняток
    return 10 / 0  # ZeroDivisionError

def middle_function():
    return inner_function()

def outer_function():
    return middle_function()

def complex_operation():
    try:
        result = outer_function()
        print("Результат:", result)
    except Exception as e:
        print("Сталася помилка:", e)
        tb = traceback.extract_tb(e.__traceback__)  # Отримуємо список фреймів стеку
        print("\nТрасування стеку:")
        for frame in tb:
            print(f"Файл: {frame.filename}")
            print(f"Рядок: {frame.lineno}")
            print(f"Функція: {frame.name}")
            print(f"Код: {frame.line}")
            print("---")
complex_operation()
# 5.1 Модуль traceback
#import traceback
#
# def function_c():
#     return 1/0
#
# def function_b():
#     function_c()
#
# def function_a():
#     try:
#         function_b()
#     except ZeroDivisionError as e:
#         print("Сталося виключення:")
#         traceback.print_exc()
# function_a()
#+++++++++++++++++++++++++++++++++++++++
# Функція traceback.print_exc()
# try:
#     1 / 0
# except ZeroDivisionError:
#     traceback.print_exc()
#+++++++++++++++++++++++++++++++++++++++++++
# Функція traceback.format_exc()
# try:
#     1 / 0
# except ZeroDivisionError:
#     error_message = traceback.format_exc()
#     print("Отриманий стек-трейс як рядок:")
#     print(error_message)
#++++++++++++++++++++++++++++++++++++++++++
#5.2 Обробка і аналіз стек-трейс
#Функція traceback.format_tb(tb)
# import sys
# import traceback
#
# def function_c():
#     return 1 / 0  # Це викличе ZeroDivisionError
#
# def function_b():
#     function_c()
#
# def function_a():
#     try:
#         function_b()
#     except ZeroDivisionError:
#         tb = sys.exc_info()[2]
#         formatted_tb = traceback.format_tb(tb)
#         print("Форматований стек-трейс:")
#         for line in formatted_tb:
#             print(line, end="")
#
# function_a()
#+++++++++++++++++++++++++++++++++++++++++++++++++++
#Функція traceback.format_exception(exc_type, exc_value, exc_tb)
# import sys
# import traceback
#
# def function_c():
#     return 1 / 0  # Це викличе ZeroDivisionError
#
# def function_b():
#     function_c()
#
# def function_a():
#     try:
#         function_b()
#     except ZeroDivisionError as e:
#         exc_type, exc_value, exc_tb = sys.exc_info()
#         full_tb = traceback.format_exception(exc_type, exc_value, exc_tb)
#         print("Повний форматований стек-трейс:")
#         for line in full_tb:
#             print(line, end="")
#
# function_a()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Іноді корисно більш детально розбирати кожен фрейм стека, щоб отримати конкретну інформацію про
 місце, де сталося виключення, і про контекст цього місця.
'''
# import traceback
# import sys
#
# def function_c():
#     return 1 / 0  # Це викличе ZeroDivisionError
#
# def function_b():
#     function_c()
#
# def function_a():
#     try:
#         function_b()
#     except ZeroDivisionError:
#         tb = sys.exc_info()[2]
#         for frame in traceback.extract_tb(tb):
#             print(f"Файл: {frame.filename}")
#             print(f"Лінія: {frame.lineno}")
#             print(f"Ім'я функції: {frame.name}")
#             print(f"Текст: {frame.line}")
#             print("-" * 40)
#
# function_a()
#5.3 Використання traceback для логування
import logging
import traceback
import sys

logging.basicConfig(filename='error.log', level=logging.ERROR)

def function_c():
    return 1 / 0  # Це викличе ZeroDivisionError

def function_b():
    function_c()

def function_a():
    try:
        function_b()
    except ZeroDivisionError as e:
        exc_type, exc_value, exc_tb = sys.exc_info()
        full_tb = traceback.format_exception(exc_type, exc_value, exc_tb)
        logging.error("Сталося виключення:\n%s", ''.join(full_tb))

function_a()


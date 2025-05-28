# Конструкція try-except
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Помилка: ділення на нуль.")
#+++++++++++++++++++++++++++++++++++++++++++
#Обробка кількох виключень
# try:
#     result = int("abc")
#
# except ZeroDivisionError:
#     print("Помилка: ділення на нуль.")
# except ValueError:
#     print("Помилка: некоректне значення.")
#+++++++++++++++++++++++++++++++++++++++++++++
#Перехоплення всіх виключень
# try:
# #     result = 10 / 0
# # except:
# #     print("Виникла помилка.")
#++++++++++++++++++++++++++++++++++++++++++
#Конструкція try-except-else
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Помилка: ділення на нуль.")
# else:
#     print(f"Результат: {result}")
#+++++++++++++++++++++++++
#Конструкція try-except-finally
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Помилка: ділення на нуль.")
# finally:
#     print("Цей блок виконується завжди.")
#++++++++++++++++++++++++++++++++++++++++++
#try-except-else-finally
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Помилка: ділення на нуль.")
# else:
#     print(f"Результат: {result}")
# finally:
#     print("Цей блок виконується завжди.")
#++++++++++++++++++++++++++++++++++++++++++
#3.3 Приклад try-except-else-finally
try:
    file = open("non_existent_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Помилка: файл не знайдено.")
except IOError:
    print("Помилка: помилка вводу-виводу.")
else:
    print(content)
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("Файл закрито.")
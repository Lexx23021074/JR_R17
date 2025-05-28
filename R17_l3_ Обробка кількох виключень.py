# 4.1 Перехоплення кількох виключень
# try:
# # Код, який може викликати виключення
#     result=int("abc")
# except ValueError:
#     print("Помилка: Некоректне значення")
# except ZeroDivisionError:
#     print("Помилка: Ділення на нуль")
# # Аналогічний оптимізований код
# try:
#     # Код, який може викликати виключення
#     result = int("abc")
# except (ValueError,ZeroDivisionError) as e:
#     print(f" Сталася помилка: {type(e)}")
#___________________________________________________
#Використання except NameError as var
# try:
#     print(undeclared_variable)
# except NameError as e:
#     print(f"Сталася помилка: {e}")
#     print(f"Тип помилки: {type(e)}")
#+++++++++++++++++++++++++++++++++++++++++++++
# 4.2 Область видимості змінної помилки
# try:
#     # Код, який може викликати NameError
#     print(undeclared_variable)
# except NameError as e:
#     print(f"Сталася помилка: {e}")
#     print(f"Тип помилки: {type(e)}")
# # Тут e вже недоступна, і наступний рядок викличе NameError
# # print(e)  # NameError: name 'e' is not defined
#Якщо ти хочеш зробити з виключенням щось важливе поза його блоком, то тобі потрібно зберегти його в окрему змінну
# exception=None
# try:
#     result=int("abc")
# except ValueError as e:
#     exception = e
#     print("Помилкка: не коретне значення")
# except ZeroDivisionError as e:
#     exception = e
#     print("Помилка: ділення на нуль.")
# print(exception)
#4.3 Що корисного містить в собі помилка
# try:
#     # Код, який може викликати ValueError
#     result = int("abc")
# except ValueError as e:
#     print(f"Сталася помилка: {e}")
#     print(f"Аргументи помилки: {e.args}")
#     print(f"Повідомлення про помилку: {str(e)}")
try:
    # Код, який може викликати кілька типів виключень
    result = 10 / 0
except (ValueError, ZeroDivisionError) as e:
    print(f"Сталася помилка: {e}")
    print(f"Тип помилки: {type(e)}")
    print(f"Аргументи помилки: {e.args}")
    #___________________________________________

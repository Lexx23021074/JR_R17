'''
Hапишіть функцію read_integer, яка приймає рядок і намагається перетворити його на ціле число.
 Якщо виникає ValueError, обробіть виняток та виведіть аргументи помилки і тип помилки.
  Додатково, збережіть виняток у змінній і виведіть її за межами блока except.
Вимоги:
•	Функція read_integer повинна намагатися перетворити переданий рядок
у ціле число за допомогою функції int().
•	Якщо при перетворенні рядка в ціле число виникає виняток ValueError,
функція повинна обробити цей виняток.
•	У блоці except функція повинна вивести аргументи помилки і тип помилки, використовуючи print().
•	Функція повинна зберегти виняток, що виник при обробці ValueError, у змінній.
•	Функція повинна вивести збережений виняток за межами блока except, використовуючи print().

'''
def read_integer(input_string):
    exception_instance = None
    try:
        return int(input_string)
    except ValueError as e:
        exception_instance = e
        print(f"Error arguments: {e.args}")
        print(f"Error type: {type(e)}")
    print(f"Exception instance: {exception_instance}")

# Приклад виклику функції
read_integer("abc")


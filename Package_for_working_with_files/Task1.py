# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random

text = "text.txt"
count_string = 5
N = 1000

def filewrite(count: int, file_name: str) -> None:
    with open(file_name, "a", encoding="utf-8") as f:
        for i in range(count):
            f.write(f"{random.randint(-N, N)}|{random.randint(-N, N)}\n")

filewrite(count_string, text)
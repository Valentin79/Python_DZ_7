# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

def function(file_num, file_name, file_res):
    with (open(file_num, 'r', encoding='utf-8') as f1,
          open(file_name, 'r', encoding='utf-8') as f2,
          open(file_res, 'w', encoding='utf-8') as f3
          ):

        len_num = sum(1 for _ in f1)
        len_name = sum(1 for _ in f2)
        print(len_num, len_name)

        for _ in range(max(len_num, len_name)):
            name = read_line(f2)
            num = read_line(f1)
            num_split = num.split('|')
            mult = int(num_split[0]) * float(num_split[1])
            if mult > 0:
                result = f'{name.upper()} {round(mult)}'
            elif mult < 0:
                result = f'{name.lower()} {abs(mult)}'
            f3.write(result + '\n')


def read_line(fd):
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[: -1]


if __name__ == '__main__':
    function("text.txt", "file_name2", "file3.txt")
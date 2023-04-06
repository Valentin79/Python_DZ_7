# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random
import string


def get_name(count_name: int, file_name: str) -> None:
    with open(file_name, 'a', encoding='utf8') as f:
        count = 0
        while count < count_name:
            length = random.randint(4, 7)
            letters = string.ascii_lowercase
            vowel = "aouyei"
            nick = ''.join(random.choice(letters) for i in range(length)).capitalize()
            # print(nick)
            for i in vowel:
                if i in nick:
                    print(nick, file=f)
                    count += 1
                    break


get_name(5, "file_name2")
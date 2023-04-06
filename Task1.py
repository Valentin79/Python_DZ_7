import os

final_name = "new_file" # желаемое имя
original_range = [1, 4] # остаток оригинального имени
source_ext = "txt"  # расширение исходного файла
target_ext = "data"  # расширение переименованного файла
num_digits = 3


def rename_files(original_range, final_name, num_digits, source_ext, target_ext):
    count = 1
    all_files = os.listdir('.') # создаем список всех файлов в директории
    for filename in all_files:
        if not filename.endswith(source_ext): # если файл не заканчивается на искомые буквы - переходим к следующему
            continue
        count_str = str(count).zfill(num_digits) # номер файла + нули
        old_name = filename[original_range[0] - 1:original_range[1]] # остаток исходного имени
        new_filename = "{}_{}_{}.{}".format(old_name, final_name, count_str, target_ext)
        # print(new_filename)
        os.rename(filename, new_filename)
        count += 1


rename_files(original_range, final_name, num_digits, source_ext, target_ext)

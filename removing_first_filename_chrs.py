import os
from tqdm import tqdm

folder_path = r'D:\Karaoke Kalinka - Karabass'  # Указываем путь к папке
characters = 6  # количество символов для удаления

# Получаем список всех файлов в папке
files = os.listdir(folder_path)

# Перебираем каждый файл
for file in tqdm(files):
    # Удаляем первые 6 символов из названия файла
    new_filename = file[characters:]

    # Указываем полный путь к старому и новому файлу
    old_file_path = os.path.join(folder_path, file)
    new_file_path = os.path.join(folder_path, new_filename)

    # Переименовываем файл
    os.rename(old_file_path, new_file_path)

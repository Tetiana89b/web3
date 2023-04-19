import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor


def process_folder(path):
    # Обробляємо всі файли в папці
    for file_name in os.listdir(path):
        full_path = os.path.join(path, file_name)
        if os.path.isfile(full_path):
            # Отримуємо розширення файлу
            extension = os.path.splitext(file_name)[1]
            # Створюємо папку з відповідним ім'ям розширення
            new_folder_path = os.path.join(path, extension[1:])
            os.makedirs(new_folder_path, exist_ok=True)
            # Переміщуємо файл у відповідну папку
            shutil.move(full_path, os.path.join(new_folder_path, file_name))
        elif os.path.isdir(full_path):
            # Якщо це підкаталог, обробляємо його в окремому потоці
            with ThreadPoolExecutor(max_workers=4) as executor:
                executor.submit(process_folder, full_path)


def main():

    #path = r'C:\Users\Таня\Desktop\tasks\web3\Хлам'
    path = sys.argv[1]
    # Обробляємо папку з використанням потоків
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.submit(process_folder, path)


if __name__ == '__main__':
    main()

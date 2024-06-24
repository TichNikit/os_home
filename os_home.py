import os
import time

directory = 'C:\py\pythonProject2\.venv\Home'
directory_norm = os.path.normpath(directory)
count = 0
for dirpath, dirmanes, filenames in os.walk(directory_norm):
    for file in filenames:
        full_filenames = os.path.join(dirpath, file)
        filetime = os.path.getmtime(full_filenames) #время
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) #время в норм. форме
        file_size = os.path.getsize(full_filenames) #вес
        parent_file = os.path.dirname(full_filenames) # родитель файла
        count += 1
        print(f'Обнаружен файл: {file}, Путь: {full_filenames}, Размер: {file_size} байт, Время изменения: {formatted_time}, Родительская директория: {parent_file}')
print(count)


#вывело
#Обнаружен файл: car.py, Путь: C:\py\pythonProject2\.venv\Home\car.py, Размер: 705 байт, Время изменения: 13.06.2024 14:14, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: car_class_many2.py, Путь: C:\py\pythonProject2\.venv\Home\car_class_many2.py, Размер: 846 байт, Время изменения: 17.06.2024 09:31, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: class2.py, Путь: C:\py\pythonProject2\.venv\Home\class2.py, Размер: 1786 байт, Время изменения: 17.06.2024 09:50, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: class2.py.txt, Путь: C:\py\pythonProject2\.venv\Home\class2.py.txt, Размер: 1786 байт, Время изменения: 17.06.2024 09:50, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: dop_cl.py, Путь: C:\py\pythonProject2\.venv\Home\dop_cl.py, Размер: 2560 байт, Время изменения: 18.06.2024 11:53, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: for i in.py, Путь: C:\py\pythonProject2\.venv\Home\for i in.py, Размер: 447 байт, Время изменения: 08.05.2024 12:59, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: homeework4.py, Путь: C:\py\pythonProject2\.venv\Home\homeework4.py, Размер: 421 байт, Время изменения: 02.05.2024 12:32, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: homework3.py, Путь: C:\py\pythonProject2\.venv\Home\homework3.py, Размер: 176 байт, Время изменения: 02.05.2024 09:27, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: homework3.py.txt, Путь: C:\py\pythonProject2\.venv\Home\homework3.py.txt, Размер: 176 байт, Время изменения: 02.05.2024 09:27, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: homework4.py, Путь: C:\py\pythonProject2\.venv\Home\homework4.py, Размер: 421 байт, Время изменения: 02.05.2024 12:32, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: homework4.py.txt, Путь: C:\py\pythonProject2\.venv\Home\homework4.py.txt, Размер: 421 байт, Время изменения: 02.05.2024 12:32, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: homework_def.py, Путь: C:\py\pythonProject2\.venv\Home\homework_def.py, Размер: 636 байт, Время изменения: 13.05.2024 10:36, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: homework_def.py.txt, Путь: C:\py\pythonProject2\.venv\Home\homework_def.py.txt, Размер: 636 байт, Время изменения: 13.05.2024 10:36, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: home_print_params.py, Путь: C:\py\pythonProject2\.venv\Home\home_print_params.py, Размер: 451 байт, Время изменения: 15.05.2024 11:15, Родительская директория: C:\py\pythonProject2\.venv\Home
#Обнаружен файл: os.py, Путь: C:\py\pythonProject2\.venv\Home\os.py, Размер: 2440 байт, Время изменения: 24.06.2024 18:43, Родительская директория: C:\py\pythonProject2\.venv\Home
#О#бнаружен файл: pep8.py, Путь: C:\py\pythonProject2\.venv\Home\pep8.py, Размер: 4878 байт, Время изменения: 07.05.2024 16:13, Родительская директория: C:\py\pythonProject2\.venv\Home
#16
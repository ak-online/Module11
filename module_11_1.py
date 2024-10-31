from PIL import Image
from threading import Thread
import datetime
import requests
import pandas as pd
import numpy as np

Lib1 = 'pillow & PIL'
Lib2 = 'requests'
Lib3 = 'pandas & numpy'

THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
res = []

students_marks_dict = {"student": ["Иванов", "Петров", "Сидоров"],
                       "math": [5, 3, 4],
                       "physics": [4, 5, 5],
                       "Urban": [5, 5, 5], }
students1 = pd.read_csv("StudentsPerformance.csv")


# pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.

def anonse(lib):
    print(f'========= Библиотека - {lib}: =========')

def print_time(lib, x):
    print(f'Время выполнения бюиблиотеки {lib} : {x}')

def change_color(image_path):
    print('change_color - ', image_path)
    image = Image.open(image_path)
    image = image.convert('L')
    image.save(image_path)


def resize_image(image_path):
    image = Image.open(image_path)
    image = image.resize((800, 600))
    image.save(image_path)


start = datetime.datetime.now()
anonse(Lib1)
for i in range(1, 13):
    image_path = f'./images/img_{i}.jpg'
    resize_image(image_path)
    change_color(image_path)

end = datetime.datetime.now()
print_time(Lib1, end - start)

# requests - запросить данные с сайта и вывести их в консоль.
anonse(Lib2)

def func(url):
    response = requests.get(THE_URL)
    page_response = response.json()
    res.append(page_response)


start = datetime.datetime.now()

for i in range(3):
    response = requests.get(THE_URL)
    page_response = response.json()
    res.append(page_response)

thr_1 = Thread(target=func, args=(THE_URL,))
thr_2 = Thread(target=func, args=(THE_URL,))
thr_3 = Thread(target=func, args=(THE_URL,))

thr_1.start()
thr_2.start()
thr_3.start()

thr_1.join()
thr_2.join()
thr_3.join()

end = datetime.datetime.now()

print_time(Lib2, end - start)
print(res)

# pandas & numpy- считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.

anonse(Lib3)
start = datetime.datetime.now()

s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])

print("Выбор одного элемента")
print(s["a"])
print("Выбор нескольких элементов")
print(s[["a", "d"]])
print("Срез")
print(s[1:])
print("Поэлементное сложение")
print(s + s)
print("Фильтрация > 2")
print(s[s > 2])
print("Фильтрация <=2 ")
print(s[s <= 2])

students = pd.DataFrame(students_marks_dict)
print(students)

print(students1.head())

end = datetime.datetime.now()

print_time(Lib3, end - start)

import time
from random import randint

import pandas as pd

def insertion_sort(array):
    n = len(array)

    operations = 0
    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]
            operations += 1

    return array, operations


def bucket_sort(array):
    start = time.time()

    operations = 0
    len_array = len(array)

    if len_array == 0:
        return array

    buckets = [[] for i in range(len_array)]

    min_val = array[0]
    for element in array:
        operations += 1

        if element < min_val:
            min_val = element

    max_val = array[0]
    for element in array:
        operations += 1
        if element > max_val:
            max_val = element

    # Проверка на отсортированность, чтобы не сортировать список зря
    if min_val == max_val:
        end = time.time()

        return array, operations, end-start

    for num in array:
        operations += 1

        normalize = (num - min_val) / (max_val - min_val + 0.1)
        bucket_number = int(len_array * normalize)

        buckets[bucket_number].append(num)

    for i in range(len_array):
        sort = insertion_sort(buckets[i])
        buckets[i] = sort[0]
        operations += sort[1]

    output = []
    for bucket in buckets:
        output.extend(bucket)

    end = time.time()

    return output, operations, end-start


def write_to_excel(arrs):
    df = pd.DataFrame(columns=('Длина', "Количество операций", "Время"))
    for arr in arrs:
        func = bucket_sort(arr)
        operations = func[1]
        times = f'{func[2]:.7f}'
        df.loc[len(df)] = [len(arr), operations, times]

    df["Время"] = df["Время"].astype(float)
    df.to_excel('sorted_databook.xlsx', index=False)


def create_data():
    with open('not_sorted_data.txt', 'w') as f:
        for i in range(100, 10001, 100):
            f.write(str([randint(-10000, 10000) for _ in range(i)]) + '\n')


def sort_data(i, j):
    arrs = [list(map(int, x[1:-2].split(', '))) for x in open('not_sorted_data.txt', 'r')]

    for arr in arrs:
        print(bucket_sort(arr)[i:j])

    return arrs

def menu():
    choice = input(
          '1) Создать файл с данными\n'
          '2) Отсортировать данные из файла (если они уже имеются)\n'
          'Выберите действие:\n'
    )
    if choice == '1':
        create_data()
    elif choice == '2':
        choice2 = input(
            '\n1) Вывести отсортированные списки\n'
            '2) Вывести только показатели (количество операций, время)\n'
            'Выберите действие:\n'
        )
        if choice2 == '1':
            a = sort_data(0, 1)
        elif choice2 == '2':
            a = sort_data(1, 3)
    choice3 = input(
        'Хотите записать данные в excel?\n'
        '1) Да\n'
        '2) Нет\n'
        'Выберите действие:'
    )
    if choice3 == '1':
        write_to_excel(a)

menu()

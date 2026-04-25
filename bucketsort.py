def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]

    return array


def bucket_sort(array):
    len_array = len(array)

    if len_array == 0:
        return array

    # Создание бакетов
    buckets = [[] for i in range(len_array)]

    min_val = array[0]
    for element in array:
        if element < min_val:
            min_val = element

    max_val = array[0]
    for element in array:
        if element > max_val:
            max_val = element

    # Проверка списка на отсортированность
    if min_val == max_val:
        return array

    for num in array:
        normalize = (num - min_val) / (max_val - min_val + 0.1)
        bucket_number = int(len_array * normalize)

        buckets[bucket_number].append(num)

    for i in range(len_array):
        buckets[i] = insertion_sort(buckets[i])

    output = []
    for bucket in buckets:
        output.extend(bucket)

    return output

print(bucket_sort([7, 3, 5, 2, 1]))


# функция для поиска наименьшего эл-та из массива (обычный список)

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

list = [3,5,-45873489573485479385, 35897, 3,45,64,-897978797,23,1,-5]
# print(list[find_smallest(list)])

# Ф-ия сортиорвки выбором
def selection(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr

print(selection(list))

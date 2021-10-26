# Рекурсивное сложение \ рекурсия - обращение ф-ии к самой себе
list = [4, 3, 2, 54, 5, 1, 0]

# Поиск сумы списка
def sum_l(sum):

    if len(sum) == 0:
        return 0

    for i in range(len(sum)):

        if len(sum) == 1:
            return sum[0]


        sum_all = sum[0] + sum_l(sum[1:])


    return sum_all
# print(sum_l(list))



# Рекурсивная ф-ия для подсчета кол-ва эл-ов в списке
def sum_l(sum):
    if len(sum) == 0:
        return 0

    for i in range(len(sum)):
        if len(sum) == 1:
            return 1
        all = 1 + sum_l(sum[1:])
    return all

# print(sum_l(list))


list = [32, 3,5]
# Поиск наиб числа при помощи рекурсии <<<<--------не получилось
# max = 0
# def sum_l(sum):
#
#     if len(sum) == 0:
#         return
#
#     for i in range(len(sum)):
#
#         if len(sum) == 1:
#             max = sum[0]
#             return max
#         else:
#             b = sum[0]
#             sum = sum[1:]
#             sum_l(sum)
#         print(88)
#         print(b)
#         print(max)
#
#         if max < b:
#             print(22)
#
#             max = b
#
#     return max
# print(sum_l(list))



# ***********Быстрая_сортировка************88

list_r = [3, 7, 5, 3, 89, 90, 567, 34, 23,1,2,3,4,5,5,6,7,8,7,64,3, 854, 84]

def sort(list):
    if len(list) < 2:
        return list
    else:
        centr = list[0]
        before = [i for i in list[1:] if i <= centr]
        after = [i for i in list[1:] if i > centr]
    return sort(before) + [centr] + sort(after)

print(sort(list_r))
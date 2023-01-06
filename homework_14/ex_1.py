import random


# создание матрицы
matrix_range = 0
while matrix_range <= 5:
    matrix_range = int(input("Введите желаемый размер матрицы (больше 5): "))

matrix = [[random.randrange(1, 50) for y in range(matrix_range)] for x in range(
    matrix_range)]

print("Изначальная матрица: ")
for i in range(matrix_range):
    print(matrix[i])
print("   ")


def rock_sort(list_to_sort):

    sums = []

    for y in range(matrix_range):
        column_sum = 0
        for x in range(matrix_range):
            column_sum = column_sum + list_to_sort[x][y]

        sums.append(column_sum)


    help_list = []

    for a in range(matrix_range):
        for b in range(matrix_range):
            help_list.append(list_to_sort[b][a])

        for c in range(matrix_range):
            for d in range(matrix_range-1-c):
                if help_list[d] > help_list[d+1]:
                    help_list[d], help_list[d+1] = \
                    help_list[d+1], help_list[d]
        # print(help_list)

        for i in range(matrix_range):
            if a % 2 != 0:
                list_to_sort[i][a] = help_list[i]
            if a % 2 == 0:
                list_to_sort[i][a] = help_list[-i-1]

        help_list.clear()

    print("Итоговая матрица: ")
    for n in range(matrix_range):
        print(list_to_sort[n])
    print(" ")
    print("Сумма столбцов: ")
    return sums


to_sort = matrix
print(rock_sort(to_sort))
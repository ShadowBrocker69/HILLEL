# ымшгвагшваирртзващпгрт
def buble_sort(list_to_sort: list) -> list:
    """ """
    n = len(list_to_sort)
    for i in range(n):
        for x in range(n-2, i-1 , -1):
            if list_to_sort[x] > list_to_sort[x+1]:
                list_to_sort[x], list_to_sort[x+1] = \
                list_to_sort[x+1], list_to_sort[x]

    return list_to_sort


def rock_sort(list_to_sort: list) -> list:
    """ """
    n = len(list_to_sort)
    for i in range(n):
        for x in range(n-1):
            if list_to_sort[x] > list_to_sort[x+1]:
                list_to_sort[x], list_to_sort[x+1] = \
                list_to_sort[x+1], list_to_sort[x]

    return  list_to_sort


if __name__ == "__main__":
    to_sort = [900, 4, 5, 2, 90, 3, 8, 400]
    print(buble_sort(to_sort))

    to_sort_2 = [900, 4, 5, 2, 90, 3, 8, 400]
    print(rock_sort(to_sort_2))

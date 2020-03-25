unsorted_list = [1950, 50, 3, 190, -50, 2, 5, -500, 150000, 1, 20, 0, 500]

def bubble_sort(the_list):
    n = len(the_list)
    for _ in range(n):
        i = 0
        j = 1
        while i < n - 1:
            if the_list[i] > the_list[j]:
                swap_elements(the_list, i, j)
            i += 1
            j += 1


# def swap(a, i, j):
#     a[i], a[j] = a[j], a[i]

def swap_elements(the_list, index1, index2):
    elem1 = the_list[index1]
    elem2 = the_list[index2]
    the_list[index1] = elem2
    the_list[index2] = elem1


bubble_sort(unsorted_list)
print(unsorted_list)
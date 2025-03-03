def bubble_sort_optimal(my_array):
    n = len(my_array)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                swapped = True
        if not swapped:
            break

    return my_array


print("Sorted array:", bubble_sort_optimal([5, 1, 7, 7, 3, 12, 11]))
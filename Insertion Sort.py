def insert_sort_optimal(my_array):
    n = len(my_array)
    for i in range(1,n):
        insert_index = i
        current_value = my_array[i]
        for j in range(i-1,-1,-1):
            if my_array[j] > current_value:
                my_array[j+1] = my_array[j]
                insert_index = j
            else:
                break
        my_array[insert_index] = current_value
    return my_array

print("Sorted array:", insert_sort_optimal([64, 34, 25, 12, 22, 11, 90, 5]))


def optimized_insertion_sort(my_array):
    n = len(my_array)
    for i in range(1, n):
        current_value = my_array[i]
        j = i - 1

        while j >= 0 and my_array[j] > current_value:
            my_array[j + 1] = my_array[j]
            j -= 1

        my_array[j + 1] = current_value
    return my_array


print("Sorted array:", optimized_insertion_sort([64, 34, 25, 12, 22, 11, 90, 5]))
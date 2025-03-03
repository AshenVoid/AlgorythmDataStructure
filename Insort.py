import bisect

def merge_two_lists(list1, list2):
    merged_list = list1.copy()
    for item in list2:
        bisect.insort(merged_list, item)
    return merged_list

print(merge_two_lists([2, 8, 3], [87, 75, 6]))
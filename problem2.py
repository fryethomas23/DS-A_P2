def rotated_array_search(input_list, number):
    pivot = find_pivot(input_list, 0, len(input_list)-1)
    if not pivot:
        return binary_search(input_list, number, 0, len(input_list)-1)

    if number < input_list[0]:
        return binary_search(input_list, number, pivot, len(input_list)-1)
    else:
        return binary_search(input_list, number, 0, pivot-1)


def find_pivot(input_list, start, end):
    mid = (start+end)//2
    while input_list[mid] > input_list[mid-1]:
        mid = (start+end)//2
        if input_list[mid] > input_list[end]:
            start = mid+1
        else:
            end = mid-1

    return mid


def binary_search(input_list, number, start, end):
    while start <= end:
        mid = (start+end)//2
        if number > input_list[mid]:
            start = mid+1
        elif number < input_list[mid]:
            end = mid-1
        else:
            return mid
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# 5
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# 2
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# 3
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# -1
test_function([[3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 1])
# 8
test_function([[3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 10])
# 7
test_function([[3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 5])
# 2
test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10])
# 9
test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1])
# 0
test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11])
# -1

def sort_012(input_list):
    zero_index = 0
    two_index = len(input_list)-1
    i = 0
    # print(input_list, i, zero_index, two_index)
    while i <= two_index:
        if input_list[i] == 2:
            input_list[two_index], input_list[i] = input_list[i], input_list[two_index]
            two_index -= 1
        if input_list[i] == 0:
            input_list[zero_index], input_list[i] = input_list[i], input_list[zero_index]
            zero_index += 1
        if input_list[i] == 1 or zero_index > i:
            i += 1
        # print(input_list, i, zero_index, two_index)

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
test_function([0])
# [0]
test_function([1])
# [1]
test_function([2])
# [2]
test_function([])
# []
test_function([0, 0, 0])
# [0, 0, 0]
test_function([1, 1, 1])
# [1, 1, 1]
test_function([2, 2, 2])
# [2, 2, 2]
test_function([0, 0, 2, 2])
# [0, 0, 2, 2]

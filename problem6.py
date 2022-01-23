import random


def get_min_max(ints):
    if not ints:
        return None

    minimum = ints[0]
    maximum = ints[0]
    for num in ints:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return (minimum, maximum)


# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((0, 0) == get_min_max([0, 0, 0, 0, 0, 0])) else "Fail")
print("Pass" if ((0, 1) == get_min_max([0, 0, 0, 1])) else "Fail")
print("Pass" if ((0, 1) == get_min_max([1, 0, 0, 0])) else "Fail")
print("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
print("Pass" if (None == get_min_max([])) else "Fail")

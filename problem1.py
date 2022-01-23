def sqrt(number):

    low = 0
    high = number
    while low < high:
        mid = (low + high)//2
        squared = mid**2
        if squared == number:
            return mid
        elif squared > number:
            high = mid-1
        else:
            low = mid+1

    return low


print("Pass" if (3 == sqrt(9)) else "Fail")
# 3
print("Pass" if (0 == sqrt(0)) else "Fail")
# 0
print("Pass" if (4 == sqrt(16)) else "Fail")
# 4
print("Pass" if (1 == sqrt(1)) else "Fail")
# 1
print("Pass" if (5 == sqrt(27)) else "Fail")
# 5
print("Pass" if (125 == sqrt(15625)) else "Fail")
# 125
print("Pass" if (125 == sqrt(15626)) else "Fail")
# 125

This solution uses a max heap because it can retrieve and remvove the largest element
from the input list in O(log(n)). Inserting into the max heap takes O(n). The total
run time would then be the combination of insertion and the retrival, which would be
O(n*log(n)). The space required is O(n) because the max heap.

time: O(n*log(n))
space: O(n)

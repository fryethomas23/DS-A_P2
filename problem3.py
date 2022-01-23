class MaxHeap:
    def __init__(self):
        self.heap = []
        self.top = None
        self.tail = None
        self.size = 0

    def insert(self, node):
        if self.top == None:
            self.top = 0
            self.tail = 0
            self.size += 1
            self.heap.append(node)
            return

        self.tail += 1
        self.size += 1
        self.heap.append(node)
        self.heapify_up()
        return

    def heapify_up(self):
        child_index = self.tail
        parent_index = (child_index-1)//2

        while self.heap[parent_index] < self.heap[child_index] and child_index != 0:
            self.heap[parent_index], self.heap[child_index] = self.heap[child_index], self.heap[parent_index]
            child_index = parent_index
            parent_index = (child_index-1)//2

        return

    def pop(self):
        if not self.heap:
            return None

        top = self.heap[self.top]
        self.heap[self.top] = self.heap[self.tail]
        del self.heap[self.tail]
        self.tail -= 1
        self.size -= 1

        if self.size == 0:
            self.top = None
            self.tail = None
        else:
            self.heapify_down()
        return top

    def heapify_down(self):
        parent_index = self.top
        lchild_index = 2*parent_index + 1
        rchild_index = 2*parent_index + 2

        if lchild_index > self.tail:
            lchild_index = parent_index
        if rchild_index > self.tail:
            rchild_index = parent_index

        while self.heap[lchild_index] > self.heap[parent_index] or self.heap[rchild_index] > self.heap[parent_index]:
            if self.heap[lchild_index] > self.heap[rchild_index]:
                bigger = lchild_index
            else:
                bigger = rchild_index

            self.heap[parent_index], self.heap[bigger] = self.heap[bigger], self.heap[parent_index]
            parent_index = bigger
            lchild_index = 2*parent_index + 1
            rchild_index = 2*parent_index + 2
            if lchild_index > self.tail:
                lchild_index = parent_index
            if rchild_index > self.tail:
                rchild_index = parent_index

        return

    def get_top(self):
        return self.top

    def get_size(self):
        return self.size


def rearrange_digits(input_list):
    if not input_list:
        return [0, 0]

    max_heap = MaxHeap()

    for el in input_list:
        max_heap.insert(el)

    largest_pair = ["", ""]
    insert_index = 0
    first = True
    while max_heap.get_top() != None:
        if first and max_heap.get_size() % 2 != 0:
            largest_pair[insert_index] += "0"
            first = False
            insert_index = 1
        else:
            data = max_heap.pop()
            largest_pair[insert_index] += str(data)
            first = False
            if insert_index == 0:
                insert_index = 1
            else:
                insert_index = 0

    largest_pair[0], largest_pair[1] = int(
        largest_pair[0]), int(largest_pair[1])

    # print(largest_pair)
    return largest_pair


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
# [531, 42]
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# [964, 852]
test_function([[0], [0, 0]])
# [0, 0]
test_function([[0, 1], [1, 0]])
# [1, 0]
test_function([[0, 1, 2], [1, 20]])
# [1, 20]
test_function([[], [0, 0]])
# [0, 0]

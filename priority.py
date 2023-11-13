class MinMaxPriorityQueue:
    class Element:
        def __init__(self, value):
            self.value = value
            self.min_heap_index = None
            self.max_heap_index = None

    def __init__(self):
        self.min_heap = []  # Min-heap
        self.max_heap = []  # Max-heap

    def insert(self, value):
        element = self.Element(value)
        self.min_heap.append(element)
        self.max_heap.append(element)
        element.min_heap_index = len(self.min_heap) - 1
        element.max_heap_index = len(self.max_heap) - 1
        self.heapify_up(self.min_heap, element.min_heap_index, min_heap=True)
        self.heapify_up(self.max_heap, element.max_heap_index, min_heap=False)
    
    def get_min(self):
        return self.min_heap[0].value if self.min_heap else None

    def get_max(self):
        return self.max_heap[0].value if self.max_heap else None


    def delete_min(self):
        if self.min_heap:
            min_element = self.min_heap[0]
            last_element = self.min_heap.pop()
            if self.min_heap:
                self.min_heap[0] = last_element
                last_element.min_heap_index = 0
                self.heapify_down(self.min_heap, 0, min_heap=True)

        # Synchronize max heap
        max_index = min_element.max_heap_index
        if max_index < len(self.max_heap) - 1:
            self.max_heap[max_index] = self.max_heap[-1]
            self.max_heap[max_index].max_heap_index = max_index
            self.heapify_down(self.max_heap, max_index, min_heap=False)
        self.max_heap.pop()
        return min_element.value

    def delete_max(self):
        if self.max_heap:
            max_element = self.max_heap[0]
            last_element = self.max_heap.pop()
            if self.max_heap:
                self.max_heap[0] = last_element
                last_element.max_heap_index = 0
                self.heapify_down(self.max_heap, 0, min_heap=False)

            # Synchronize min heap
            min_index = max_element.min_heap_index
            if min_index < len(self.min_heap) - 1:
                self.min_heap[min_index] = self.min_heap[-1]
                self.min_heap[min_index].min_heap_index = min_index
                self.heapify_down(self.min_heap, min_index, min_heap=True)
            self.min_heap.pop()
            return max_element.value

    def heapify_up(self, heap, index, min_heap):
        parent_index = (index - 1) // 2
        while index > 0 and ((heap[index].value < heap[parent_index].value and min_heap) or
                            (heap[index].value > heap[parent_index].value and not min_heap)):
            heap[index], heap[parent_index] = heap[parent_index], heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def heapify_down(self, heap, index, min_heap):
        size = len(heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest_or_largest = index

            if left < size and ((heap[left].value < heap[smallest_or_largest].value and min_heap) or
                                (heap[left].value > heap[smallest_or_largest].value and not min_heap)):
                smallest_or_largest = left

            if right < size and ((heap[right].value < heap[smallest_or_largest].value and min_heap) or
                                (heap[right].value > heap[smallest_or_largest].value and not min_heap)):
                smallest_or_largest = right

            if smallest_or_largest != index:
                heap[index], heap[smallest_or_largest] = heap[smallest_or_largest], heap[index]
                index = smallest_or_largest
            else:
                break

    def is_empty(self):
        return len(self.min_heap) == 0

    def size(self):
        return len(self.min_heap)
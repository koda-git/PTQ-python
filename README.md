# PTQ-python
Priority Queue with Double Heaps implemented with Python

1. **Insert**:
   - Insert the element into both the min-heap and max-heap.
   - Perform a `heapify_up` (swim up) operation on both heaps
   - Time Complexity: O(log n) as the `heapify_up` process takes O(log n) time in the worse case when it traverses the height of the heap 
2. **Delete Max**:
   - Removes the root element (max) from the `max_heap` **O(1)**
   - The last element of the max-heap is moved to index 0 (root) **O(1)**
   - Remove the synchronized maximum element that was removed just before in the `min_heap`  (We have the index for both `min_heap` and `max_heap` for that element from the `Element` subclass) **O(1)**
   - The replace the same index that was removed with the last element in `min_heap` **O(1)**
   - We use the `heapify_down` (swim down) operation starting from the new root on both the `min_heap` and `max_heap` **O(log n)**
   -  **O(log n)** as `heapify_down` can traverse the height of the heap and **O(log n) > O(1)**
3. **Delete Min**:
   - Removes the root element (min) from the `min_heap` **O(1)**
   - The last element of the min-heap is moved to index 0 (root). **O(1)**
   - Remove the synchronized minimum element that was removed just before in the `min_heap` (We have the index for both `min_heap` and max_heap for that element from the Element subclass) **O(1)**
   - The replace the same index that was removed with the last element in max_heap **O(1)**
   - We use the `heapify_down` (swim down) operation starting from the new root on both the `min_heap` and `max_heap` **O(log n)**
   - **O(log n)** as `heapify_down` can traverse the height of the heap and **O(log n) > O(1)**
4. **Find Max**:
   - Return the root element of the `max-heap`
   - Time Complexity: **O(1)**, as the max element is always at the root (index 0) of the `max-heap`
5. **Find Min**:
   - Return the root element of the `min_heap`
   - Time Complexity: **O(1)**, as the min element is always at the root (index 0) of the `min_heap`

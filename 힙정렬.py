# 힙 자료구조
class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
    
    def _sift_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)
    
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if len(self.heap) > 0:
            self._sift_down(0)
        
        return max_val
    
    def _sift_down(self, i):
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
        
        if i != max_index:
            self.swap(i, max_index)
            self._sift_down(max_index)

# 힙 정렬
def heap_sort(arr):
    # 최대 힙 구성
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    
    # 최대 힙 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # 힙에서 요소를 하나씩 추출
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

# 테스트
print("힙 자료구조 테스트")
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(15)
heap.insert(30)
print("힙 상태:", heap.heap)
print("최대값 추출:", heap.extract_max())
print("힙 상태:", heap.heap)

print("\n힙 정렬 테스트")
arr = [64, 25, 12, 22, 11]
print("정렬 전:", arr)
sorted_arr = heap_sort(arr)
print("정렬 후:", sorted_arr) 
# 삽입정렬(Insertion Sort)# 장점   
# - 최선의 경우 O(N)이라는 엄청나게 빠른 효율성을 가지고 있다.    
# - 성능이 좋아서 다른 정렬 알고리즘의 일부로 사용될 만큼 좋은 정렬법이다.
# # 단점  
# - 최악의 경우 n**2 이라는 시간복잡도를 갖게된다
# 즉, 데이터의 상태 및 데이터의 크기에 따라서 성능의 편차가 굉장히 심한 정렬법

# 단순 삽입 정렬 (Insertion Sort)
def insertion_sort(arr):
    n = len(arr)
    
    # 두 번째 원소부터 시작
    for i in range(1, n):
        # 현재 원소를 임시 저장
        key = arr[i]
        # 정렬된 부분의 마지막 인덱스
        j = i - 1
        
        # key보다 큰 원소들을 한 칸씩 뒤로 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # key를 적절한 위치에 삽입
        arr[j + 1] = key
    
    return arr

# 테스트
arr = [64, 25, 12, 22, 11]
print("정렬 전:", arr)

# 정렬 과정을 보여주는 예시
print("\n정렬 과정:")
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    print(f"\n{key}를 삽입하는 과정:")
    print(f"현재 상태: {arr[:i]} | {arr[i:]}")  # 정렬된 부분 | 정렬되지 않은 부분
    
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
        print(f"이동 후: {arr[:i]} | {arr[i:]}")
    
    arr[j + 1] = key
    print(f"삽입 후: {arr[:i+1]} | {arr[i+1:]}")

print("\n정렬 후:", arr)

# ===========================================
# 이진 삽입 정렬 (Binary Insertion Sort)
def binary_search(arr, key, left, right):
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= key:
            left = mid + 1
        else:
            right = mid
    return left

def binary_insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        # 이진 탐색으로 삽입 위치 찾기
        pos = binary_search(arr, key, 0, i)
        
        # pos부터 i까지의 원소들을 한 칸씩 뒤로 이동
        for j in range(i, pos, -1):
            arr[j] = arr[j-1]
        
        # key를 적절한 위치에 삽입
        arr[pos] = key
    
    return arr

# 테스트
print("\n이진 삽입 정렬 테스트")
arr = [64, 25, 12, 22, 11]
print("정렬 전:", arr)

# 정렬 과정을 보여주는 예시
print("\n정렬 과정:")
for i in range(1, len(arr)):
    key = arr[i]
    pos = binary_search(arr, key, 0, i)
    print(f"\n{key}를 삽입하는 과정:")
    print(f"현재 상태: {arr[:i]} | {arr[i:]}")
    print(f"이진 탐색으로 찾은 삽입 위치: {pos}")
    
    # 이동 과정
    for j in range(i, pos, -1):
        arr[j] = arr[j-1]
        print(f"이동 후: {arr[:i]} | {arr[i:]}")
    
    arr[pos] = key
    print(f"삽입 후: {arr[:i+1]} | {arr[i+1:]}")

print("\n정렬 후:", arr)



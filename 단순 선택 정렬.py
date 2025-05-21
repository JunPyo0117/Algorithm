# 단순 선택 정렬
# 장점   
# - 선택정렬 또한 버블정렬과 마찬가지로 구현이 쉬운편에 속하는 정렬법   
# - 정렬을 위한 비교 횟수는 많지만 실제로 교환하는 횟수는 적기 때문에 많은 교환이 일어나야 하는 자료상태에서 효율적으로 사용될 수 있다.
# - 버블정렬과 비교했을 때, 똑같이  n**2 이라는 시간복잡도를 갖지만, 실제로 시간을 측정해보면 버블정렬에 비해서는 조금 더 빠른 정렬 방식
# ===========================================
# 선택 정렬 (Selection Sort)
def selection_sort(arr):
    n = len(arr)
    
    # 각 위치에 들어갈 최소값을 찾아 정렬
    for i in range(n):
        # 현재 위치부터 끝까지 중 최소값의 인덱스를 찾음
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # 최소값을 현재 위치로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# 테스트
arr = [64, 25, 12, 22, 11]
print("정렬 전:", arr)

# 정렬 과정을 보여주는 예시
print("\n정렬 과정:")
for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(f"단계 {i+1}:", arr)

print("\n정렬 후:", arr)

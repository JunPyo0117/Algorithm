# 퀵 정렬(Quick Sort)
# # 장점   
# - 기준값에 의한 분할을 통해서 구현하는 정렬법으로써, 분할 과정에서 logN 이라는 시간이 걸리게되고 전체적으로 보게 되면 NlogN 으로써 실행시간이 준수한 편이다.
# # 단점   
# - 기준값(Pivot)에 따라서 시간복잡도가 크게 달라진다. 
# - Pivot이 적당하게 이상적인 값을 선택했다면 NlogN의 시간복잡도를 갖지만, 최악으로 Pivot을 선택할 경우 n**2 이라는 시간복잡도를 가짐

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 피벗 선택 (여기서는 첫 번째 원소)
    pivot = arr[0]
    
    # 피벗보다 작은 원소들
    left = [x for x in arr[1:] if x <= pivot]
    # 피벗보다 큰 원소들
    right = [x for x in arr[1:] if x > pivot]
    
    # 재귀적으로 정렬하고 결과 합치기
    return quick_sort(left) + [pivot] + quick_sort(right)

# 개선된 퀵 정렬 (in-place 정렬)
def quick_sort_in_place(arr, low, high):
    def partition(low, high):
        # 피벗을 마지막 원소로 선택
        pivot = arr[high]
        i = low - 1  # 피벗보다 작은 원소들의 마지막 인덱스
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # 피벗을 올바른 위치로 이동
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    if low < high:
        # 분할
        pivot_index = partition(low, high)
        # 왼쪽 부분 정렬
        quick_sort_in_place(arr, low, pivot_index - 1)
        # 오른쪽 부분 정렬
        quick_sort_in_place(arr, pivot_index + 1, high)

# 테스트
print("기본 퀵 정렬 테스트")
arr1 = [64, 25, 12, 22, 11]
print("정렬 전:", arr1)
sorted_arr1 = quick_sort(arr1)
print("정렬 후:", sorted_arr1)

print("\n개선된 퀵 정렬 테스트")
arr2 = [64, 25, 12, 22, 11]
print("정렬 전:", arr2)
quick_sort_in_place(arr2, 0, len(arr2) - 1)
print("정렬 후:", arr2)

# 정렬 과정을 보여주는 예시
print("\n정렬 과정 예시:")
arr3 = [64, 25, 12, 22, 11]
print("초기 배열:", arr3)

def quick_sort_with_steps(arr, depth=0):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    print("  " * depth + f"피벗: {pivot}")
    print("  " * depth + f"왼쪽: {left}")
    print("  " * depth + f"오른쪽: {right}")
    
    return quick_sort_with_steps(left, depth + 1) + [pivot] + quick_sort_with_steps(right, depth + 1)

print("\n정렬 과정:")
quick_sort_with_steps(arr3)


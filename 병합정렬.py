# 병합 정렬(Merge Sort)
# 장점
# - 안정적인 정렬 알고리즘
# - 최악의 경우에도 O(n log n)의 시간 복잡도
# - 대규모 데이터 정렬에 효율적
# 단점
# - 추가 메모리 공간이 필요 (O(n))
# - 작은 데이터셋에서는 다른 정렬보다 느릴 수 있음

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 배열을 두 개의 균등한 부분으로 분할
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # 각 부분을 재귀적으로 정렬
    left = merge_sort(left)
    right = merge_sort(right)
    
    # 정렬된 두 부분을 병합
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # 두 배열의 원소를 비교하며 병합
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 남은 원소들을 결과 배열에 추가
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# 정렬 과정을 보여주는 개선된 병합 정렬
def merge_sort_with_steps(arr, depth=0):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    print("  " * depth + f"분할: {arr} -> {left} | {right}")
    
    left = merge_sort_with_steps(left, depth + 1)
    right = merge_sort_with_steps(right, depth + 1)
    
    result = merge(left, right)
    print("  " * depth + f"병합: {left} + {right} -> {result}")
    
    return result

# 테스트
print("기본 병합 정렬 테스트")
arr1 = [64, 25, 12, 22, 11]
print("정렬 전:", arr1)
sorted_arr1 = merge_sort(arr1)
print("정렬 후:", sorted_arr1)

print("\n정렬 과정이 보이는 병합 정렬 테스트")
arr2 = [64, 25, 12, 22, 11]
print("초기 배열:", arr2)
print("\n정렬 과정:")
merge_sort_with_steps(arr2)

# 추가 테스트 케이스
print("\n추가 테스트 케이스")
arr3 = [38, 27, 43, 3, 9, 82, 10]
print("정렬 전:", arr3)
sorted_arr3 = merge_sort(arr3)
print("정렬 후:", sorted_arr3)

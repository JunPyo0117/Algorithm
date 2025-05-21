# 버블 정렬
# - 일단 구현이 쉬움
# - Bubble정렬은 인접한 값만 계속해서 비교하면 되는 방식으로 굉장히 구현이 쉬운편
# - 코드 자체가 직관적
# 단점   
# - 굉장히 비효율적
# - 최악이든 최선이든 n**2 이라는 시간복잡도를 갖기 때문에 사실 알고리즘에서 효율적인 정렬방법으로 사용되지는 않는다.


def bubble(num_list):
    n = len(num_list)
    for i in range(n):
        for j in range(n-i-1):
            if num_list[j] > num_list[j +1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

num_list = [ 5, 6, 7, 3, 9, 4]

bubble(num_list)

print(num_list)

# ========================================================
# 버블 정렬 / 이미 정렬된 부분을 다시 검사하지 않도록 최적화
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 교환이 일어났는지 확인하는 플래그
        swapped = 0
        # 마지막 i개의 요소는 이미 제자리에 있으므로 검사하지 않음
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped += 1
        
        # 교환이 일어나지 않았다면 정렬이 완료된 것
        if swapped ==0:
            break
    
    return arr

# 테스트
arr = [64, 34, 25, 12, 22, 11, 90]
print("정렬 전:", arr)
print("정렬 후:", bubble_sort(arr))

# ============================================
# 셰이커 정렬 (Shaker Sort)
def shaker_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    
    while left < right:
        # 왼쪽에서 오른쪽으로 (가장 큰 값을 오른쪽으로)
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1
        
        # 오른쪽에서 왼쪽으로 (가장 작은 값을 왼쪽으로)
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
    
    return arr

# 테스트
arr = [64, 34, 25, 12, 22, 11, 90]
print("정렬 전:", arr)
print("정렬 후:", shaker_sort(arr))
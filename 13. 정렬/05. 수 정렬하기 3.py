# import sys

# n = int(sys.stdin.readline())

# arr = []

# for _ in range(n):
#     arr.append(int(sys.stdin.readline()))


# cnt_arr = [0] * (max(arr) + 1) 

# for num in arr:
#     cnt_arr[num] += 1

# for i in range(1, len(cnt_arr)):
#     cnt_arr[i] += cnt_arr[i-1]


# result = [0] * (len(arr))

# for num in arr:
#     idx = cnt_arr[num]
#     result[idx -1] = num
#     cnt_arr[num] -= 1

# print('\n'.join(map(str, result)))

# =========================================
import sys
input = sys.stdin.readline

# 계수(도수)정렬 활용
n = int(input())
arr = [0] * (10000 + 1)  # 입력값이 10000개까지 주어지니 10000 + 1개의 리스트 선언


# 각 입력값에 해당하는 인덱스의 값 증가
for _ in range(n):
    arr[int(input())] += 1

print(arr)

# arr에 기록된 정보 확인
for i in range(len(arr)):
    if arr[i] != 0:  # 0이 아닌 데이터, 즉 입력받은 데이터들을 출력
        for _ in range(arr[i]):
            print(i)
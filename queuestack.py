# import sys
# input = sys.stdin.readline
# from collections import deque

# # 입력
# n = int(input())  # 자료구조 개수
# a = list(map(int, input().split()))  # 0: 큐, 1: 스택
# b = list(map(int, input().split()))  # 초기 자료구조 안 값
# m = int(input())  # 삽입할 수열의 길이
# c = list(map(int, input().split()))  # 삽입할 수열

# # 자료구조 초기화
# structures = []
# for i in range(n):
#     if a[i] == 0:
#         structures.append(deque([b[i]]))  # 큐: 덱 사용
#     else:
#         structures.append([b[i]])  # 스택: 리스트 사용

# # 결과 저장
# result = []

# for num in c:
#     x = num
#     for i in range(n):
#         # 삽입
#         if a[i] == 0:  # 큐
#             structures[i].append(x)
#             x = structures[i].popleft()
#         else:  # 스택
#             structures[i].append(x)
#             x = structures[i].pop()
#     result.append(x)

# # 출력
# print(*result)
# =======================
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())                    # queuestack을 구성하는 N개의 자료구조
A = list(map(int, input().split())) # 길이 N의 수열 A
B = list(map(int, input().split())) # 길이 N의 수열 B
M = int(input())                    # 삽입할 수열의 길이 M
C = list(map(int, input().split())) # 길이 M의 수열 C

queue = deque([])
for i in range(N):
    if A[i] == 0: # 큐인 자료구조만 모으기
        queue.append(B[i])

# print(queue)

# 배열 C의 원소를 1개 appendleft 할 때마다 pop 연산 수행
for i in C:
    queue.appendleft(i)
    print(queue.pop(), end= ' ')

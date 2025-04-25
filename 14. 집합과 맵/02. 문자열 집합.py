import sys

# N과 M 입력 받기
n, m = map(int, sys.stdin.readline().split())

# N개의 문자열을 집합으로 저장
set_n = set(sys.stdin.readline().strip() for _ in range(n))

# M개의 문자열을 확인하며 카운트
cnt = 0
for _ in range(m):
    if sys.stdin.readline().strip() in set_n:
        cnt += 1

print(cnt)

# ========================
# 리스트를 이용하면 시간 초과
# import sys

# n, m = map(int, sys.stdin.readline().split())

# list_n = [sys.stdin.readline().strip() for _ in range(n)]
# list_m = [sys.stdin.readline().strip() for _ in range(m)]

# cnt = 0
# for m in list_m:
#     if m in list_n:
#         cnt += 1
# print(cnt)
import sys

# n, m 입력
n, m = map(int, sys.stdin.readline().split())

# 입력값 set으로 받기
n_set = set(map(int, sys.stdin.readline().split()))
m_set = set(map(int, sys.stdin.readline().split()))

# print(n_set, m_set)
# 대칭 차집합 구하기 (A-B)+(B-A), ^ 
print(len(n_set - m_set) + len(m_set - n_set))
print(len(n_set ^ m_set))
import sys

# n, m 입력
n, m = map(int, sys.stdin.readline().split())

# 듣지 못한 이름, 보지 못한 이름 입력
never_listen_name = set(sys.stdin.readline().strip() for _ in range(n))
never_saw_name = set(sys.stdin.readline().strip() for _ in range(m))

# print(never_listen_name)
# print(never_saw_name)

# 듣지 못한 이름과 보지 못한 이름의 교집합 구함
never_listen_saw_name = never_listen_name & never_saw_name

# 듣보잡의 길이(사람 수) 출력
print(len(never_listen_saw_name))

# 듣보잡의 이름 사전순으로 출력
for i in sorted(never_listen_saw_name):
    print(i)

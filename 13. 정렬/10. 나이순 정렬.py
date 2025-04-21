import sys

input = sys.stdin.readline

n = int(input())

old_name = [list(input().split()) for _ in range(n)]

# print(old_name)

old_name.sort(key=lambda x: int(x[0]))      # int로 해야 오름차순으로 된다. int가 없으면 문자열로 취급 되어 같은 문자끼리만 묶임

for data in old_name:
    print(*data)       # 2차원 배열 출력시 각 인덱스 출력
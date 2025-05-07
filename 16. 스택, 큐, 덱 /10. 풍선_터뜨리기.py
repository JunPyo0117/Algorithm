import sys
from collections import deque

n = int(input())
# (풍선 번호, 이동할 숫자) 형태로 저장
balloons = deque(enumerate(map(int, sys.stdin.readline().split()), 1))
result = []

while balloons:
    # 현재 풍선의 번호와 이동할 숫자를 가져옴
    idx, move = balloons.popleft()
    result.append(idx)
    
    if balloons:  # 풍선이 남아있다면
        # 양수면 왼쪽으로, 음수면 오른쪽으로 회전
        if move > 0:
            balloons.rotate(-(move - 1))
        else:
            balloons.rotate(-move)

print(*result)

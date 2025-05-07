import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque(range(1, n+1))

while True:
    if len(card) == 1:
        print(card[0])
        break

    card.popleft()
    card.append(card.popleft())


import sys 
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == '1':  # push left
        queue.appendleft(int(command[1]))
    elif command[0] == '2':  # push right
        queue.append(int(command[1]))
    elif command[0] == '3':  # pop left
        print(queue.popleft() if queue else -1)
    elif command[0] == '4':  # pop right
        print(queue.pop() if queue else -1)
    elif command[0] == '5':  # size
        print(len(queue))
    elif command[0] == '6':  # empty
        print(1 if not queue else 0)
    elif command[0] == '7':  # left
        print(queue[0] if queue else -1)
    elif command[0] == '8':  # right
        print(queue[-1] if queue else -1)
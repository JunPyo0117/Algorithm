import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
stack = []
number = 1


for i in range(n):
    if num_list[i] == number:
        number += 1
    else:
        stack.append(num_list[i])

    for j in range(len(stack)):
        if stack[-1] == number:
            number += 1
            stack.pop()

if not stack:    
    print("Nice")
else:
    print("Sad")
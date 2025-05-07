c
stack = []

for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == '1':  # push
        stack.append(int(command[1]))
    elif command[0] == '2':  # pop
        print(stack.pop() if stack else -1)
    elif command[0] == '3':  # size
        print(len(stack))
    elif command[0] == '4':  # empty
        print(1 if not stack else 0)
    elif command[0] == '5':  # top
        print(stack[-1] if stack else -1)


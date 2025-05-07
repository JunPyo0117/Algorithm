import sys


while True:
    my_string = sys.stdin.readline().rstrip()
    if my_string == ".":
        break

    stack = []
    valid = True

    for char in my_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                valid = False
                break
            stack.pop()
        elif char == "[":
            stack.append(char)
        elif char == "]":
            if not stack or stack[-1] != "[":
                valid = False
                break
            stack.pop()

    
    if valid and not stack:
        print("yes")
    else:
        print("no")
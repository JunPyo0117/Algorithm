import sys
input = sys.stdin.readline

def fibonacci2(n):
    a, b = 0, 1  
    for _ in range(2, n + 1):
        a, b = b, a + b  
    return b

print(fibonacci2(int(input())))


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(int(input())))
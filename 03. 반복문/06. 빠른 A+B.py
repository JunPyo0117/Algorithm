import sys

t= input()

for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
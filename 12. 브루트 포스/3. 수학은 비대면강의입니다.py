# 근의 공식
import sys
a,b,c,d,e,f = map(int, sys.stdin.readline().split())

y = (a*f - d*c) // (a*e - d*b)
x = (e*c - b*f) // (a*e - d*b)

print(x, y)


# ======================
# 부르트 포스
import sys
a,b,c,d,e,f = map(int, sys.stdin.readline().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
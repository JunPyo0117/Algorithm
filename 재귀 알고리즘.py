# 팩토리얼
def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1
    
n = 10

print(factorial(5))

# =======================================
# 반복문 while로 풀기
import sys

input = sys.stdin.readline

n = int(input())

multi_num = 1  # 초기값을 1로 설정

while n > 0:
    multi_num *= n 
    n = n - 1 

print(multi_num)

# ========================================
# 최대공약수 GCD
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y ,x%y)

print(gcd(144, 60))
# =====================================
# 재귀함수 분석

def recur(n):
    if n >0:
        recur(n-1)
        print(n)
        recur(n-2)
 
print(4)

# 꼬리 재귀 제거
def recur(n):
	while n > 0:
          recur(n-1)
          print(n)
          n = n - 2

# 재귀 제거
from stack import Stack

def recur(n:int)->int:
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n-1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break
# =================================
# 하노이의 탑
def move(no, x, y):
    if no > 1:
        move(no -1, x, 6-x-y)

        print(f'원반 [{no}]을 {x}기둥에서 {y} 기둥으로 옮깁니다.')

        if no > 1:
            move(no-1, 6-x-y, y)

print('하노이의 탑을 구현합니다.')
n = int(input('원반의 개수를 입력하세요.: '))

move(n, 2, 3)

# ====================================
# 피보나치 수열
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(int(input())))
# ===========================================
# 반복문으로 풀기
def fibonacci2(n):
    a, b = 0, 1  # 초기값 설정
    for _ in range(2, n + 1):
        a, b = b, a + b  # 다음 피보나치 수 계산
    return b

print(fibonacci(int(input())))

# ===========================================


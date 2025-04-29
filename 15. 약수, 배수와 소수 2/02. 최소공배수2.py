# 빠른 입력을 위한 라이브러리
import sys
# 최소공배수(lcm)와 최대공약수(gcd) 계산을 위한 라이브러리
import math

# 최소공배수를 구하는 함수 (주석 처리된 코드)
# def lcm(num1, num2):
#     for i in range(max(num1, num2), num1*num2 + 1):
#         if i % num1 == 0 and i % num2 == 0:
#             return i

# 두 정수 A, B 입력
A, B = map(int, sys.stdin.readline().split())

# math.lcm 함수로 최소공배수 계산 및 출력
print(math.lcm(A, B))
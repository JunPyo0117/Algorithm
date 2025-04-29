# 빠른 입력을 위한 라이브러리
import sys
# 최소공배수(lcm)와 최대공약수(gcd) 계산을 위한 라이브러리
import math

# 테스트 케이스의 수 입력
T = int(sys.stdin.readline())

# 각 테스트 케이스마다 처리
for _ in range(T):
    # 두 정수 A, B 입력
    A, B = map(int, sys.stdin.readline().split())
    # math.lcm 함수로 최소공배수 계산 및 출력
    print(math.lcm(A, B))
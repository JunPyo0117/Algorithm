# 빠른 입력을 위한 라이브러리
import sys

# M 이상 N 이하의 소수를 모두 출력하는 함수
def is_prime_fast(num):
    # 2 미만의 수는 소수가 아님
    if num < 2:
        return False
    # 2는 소수
    if num == 2:
        return 2
    # 2로 나누어 떨어지는 수는 소수가 아님
    if num % 2 == 0:
        return False
    # 3부터 sqrt(num)까지의 홀수로만 나누어봐서 검사 횟수 감소
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# M과 N 입력
m, n = map(int, sys.stdin.readline().split())

# M 이상 N 이하의 소수를 모두 출력
for i in range(m, n+1):
    if is_prime_fast(i):
        print(i)

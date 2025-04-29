import sys

# 기본적인 소수 판별 함수
# 입력받은 숫자가 소수인지 확인
# 2부터 입력받은 숫자보다 작은 모든 수로 나누어봄
# 나누어 떨어지는 수가 있으면 소수가 아님
# 모든 수로 나누어도 나누어 떨어지지 않으면 소수
def is_prime(num1):
    for i in range(2, num1):
        if num1 % i == 0:
            break
    else:
        return num1

# 주어진 숫자보다 크거나 같은 가장 작은 소수 찾기
# 2 이하의 수는 다음 소수가 2
# 현재 숫자부터 시작하여 소수를 찾을 때까지 1씩 증가하며 검사
def next_prime_funtion(num1):
    if num1 <= 2:
        return 2
    current = num1
    while True:
        if is_prime(current):
            return current
        current += 1

# 테스트 케이스의 수 입력
a = int(sys.stdin.readline())

# 각 테스트 케이스마다 처리
for _ in range(a):
    n = int(sys.stdin.readline())
    next_prime = next_prime_funtion(n)
    print(next_prime)

# ===================
import sys 

# 시간 제한을 맞추기 위한 최적화된 소수 판별 함수
# 2 미만의 수는 소수가 아님
# 2는 소수
# 2로 나누어 떨어지는 수는 소수가 아님
# 3부터 sqrt(n)까지의 홀수로만 나누어봐서 검사 횟수 감소
def is_prime_fast(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# 주어진 숫자보다 크거나 같은 가장 작은 소수 빠르게 찾기
# 1 이하의 수는 다음 소수가 2
# 2는 이미 소수이므로 그대로 반환
# 짝수인 경우 홀수로 변경 후 검사 시작
# 홀수만 검사하여 검사 횟수 감소
def find_next_prime_fast(n):
    if n <= 1:
        return 2
    if n == 2:
        return 2
    if n % 2 == 0:
        n += 1
    while not is_prime_fast(n):
        n += 2
    return n

# 최적화된 함수를 사용하여 다음 소수 찾기
# 테스트 케이스의 수 입력
a = int(sys.stdin.readline())
# 각 테스트 케이스마다 처리
for _ in range(a):
    n = int(sys.stdin.readline())
    next_prime = find_next_prime_fast(n)
    print(next_prime)
    


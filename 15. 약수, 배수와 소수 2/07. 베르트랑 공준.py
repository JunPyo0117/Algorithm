import sys

# 소수 판별 함수 (제곱근 최적화 방법)
def is_prime(n):
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

# 0을 입력받을 때까지 반복
while True:
    # n 입력
    n = int(sys.stdin.readline())
    
    # 0이 입력되면 종료
    if n == 0:
        break
    
    # n+1부터 2n까지의 소수 개수 계산
    count = 0
    for i in range(n+1, 2*n+1):
        if is_prime(i):
            count += 1
    
    # 결과 출력
    print(count)

# ===================
# 더 간단한 방법 (에라토스테네스의 체 사용)
import sys

# 소수 배열 초기화 (False: 소수 아님, True: 소수)
is_prime = [False, False] + [True] * 246912  # 2*123456 = 246912

# 에라토스테네스의 체로 소수 표시
for i in range(2, int(246912 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, 246913, i):
            is_prime[j] = False

# 0을 입력받을 때까지 반복
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    # n+1부터 2n까지의 소수 개수 계산
    count = sum(is_prime[n+1:2*n+1])
    print(count)
    
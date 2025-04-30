# sys 모듈을 사용해 빠른 입력을 받기 위해 import
import sys

# 0과 1은 소수가 아니므로 False, 나머지 999,999개를 True로 초기화 (소수 판별용)
is_prime = [False, False] + [True] * 999999  

# 에라토스테네스의 체 알고리즘으로 소수 목록을 미리 구함
for i in range(2, int(1000000 ** 0.5) + 1):  # 2부터 √1,000,000까지 반복
    if is_prime[i]:  # i가 소수이면
        for j in range(i*i, 1000000, i):  # i의 배수들은 소수가 아니므로
            is_prime[j] = False  # 해당 인덱스를 False로 마킹

# 테스트 케이스 개수 입력
t = int(sys.stdin.readline())

# 테스트 케이스 수만큼 반복
for _ in range(t):
    cnt = 0  
    n = int(sys.stdin.readline())
    for a in range(2, n//2 + 1):
        b = n - a  
        if is_prime[a] and is_prime[b]:  # a와 b가 모두 소수이면
            cnt += 1  
    print(cnt)  
# ==================================


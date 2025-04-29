# 빠른 입력을 위한 라이브러리
import sys
# 최대공약수(gcd) 계산을 위한 라이브러리
import math

# 첫 번째 분수의 분자(A1)와 분모(B1) 입력
A1, B1 = map(int, sys.stdin.readline().split())
# 두 번째 분수의 분자(A2)와 분모(B2) 입력
A2, B2 = map(int, sys.stdin.readline().split())

# 분수 덧셈 결과 계산
# 분자 = (A1*B2 + A2*B1)
child = (A1*B2 + A2*B1)
# 분모 = B1 * B2
parent = B1 * B2

# 분자와 분모의 최대공약수가 1이 아니면 기약분수로 변환
if math.gcd(child, parent) != 1:
    # 분자와 분모를 최대공약수로 나누어 기약분수로 변환
    print(child//math.gcd(child, parent), parent//math.gcd(child, parent))
# 분자와 분모의 최대공약수가 1이면 이미 기약분수이므로 그대로 출력
else:
    print(child, parent)
    




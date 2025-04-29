# 빠른 입력을 위한 라이브러리
import sys
# 최대공약수(gcd) 계산을 위한 라이브러리
import math
# 리스트의 모든 요소에 대해 함수를 적용하기 위한 라이브러리
from functools import reduce

# 가로수의 개수 입력
n = int(sys.stdin.readline())

# 가로수의 위치를 입력받아 리스트에 저장
garosu = [int(sys.stdin.readline().strip()) for _ in range(n)]

# 인접한 가로수 간의 차이를 계산하여 리스트에 저장
differences = []
for i in range(len(garosu) - 1):
    diff = garosu[i+1] - garosu[i]
    differences.append(diff)

# 모든 차이값의 최대공약수 계산
gcd = reduce(math.gcd, differences)

# 추가해야 할 가로수의 개수 계산
# 첫 번째 가로수부터 마지막 가로수까지 gcd 간격으로 놓았을 때의 가로수 개수에서
# 이미 있는 가로수 개수를 빼면 추가해야 할 가로수 개수가 됨
total_trees = ((garosu[-1] - garosu[0]) // gcd) + 1
additional_trees = total_trees - n

# 추가해야 할 가로수의 개수 출력
print(additional_trees)
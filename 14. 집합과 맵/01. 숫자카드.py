# 빠른 입력을 위한 라이브러리 임포트
import sys

# 숫자카드 개수 입력
n = int(sys.stdin.readline())
# 숫자카드 입력
card = list(map(int, sys.stdin.readline().split()))

# 확인할 숫자카드 개수 입력
m = int(sys.stdin.readline())
# 확인할 숫자카드 입력
check = list(map(int, sys.stdin.readline().split()))

# 숫자카드 정렬
card.sort()

# 확인할 숫자카드 탐색
for i in range(m):
    # 확인할 숫자카드가 숫자카드 리스트에 있으면 1 출력, 없으면 0 출력
    if check[i] in card:
        print(1, end=' ')
    else:
        print(0, end=' ')

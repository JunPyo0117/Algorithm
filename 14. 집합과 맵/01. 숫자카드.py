# # 모든 숫자카드를 확인하는 방법
# # 빠른 입력을 위한 라이브러리 임포트
# import sys

# # 숫자카드 개수 입력
# n = int(sys.stdin.readline())
# # 숫자카드 입력
# card = set(map(int, sys.stdin.readline().split()))

# # 확인할 숫자카드 개수 입력
# m = int(sys.stdin.readline())
# # 확인할 숫자카드 입력
# check = list(map(int, sys.stdin.readline().split()))

# # 확인할 숫자카드 탐색
# for i in range(m):
#     # 확인할 숫자카드가 숫자카드 리스트에 있으면 1 출력, 없으면 0 출력
#     if check[i] in card:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

# ========================================================
# dictionary 사용
# import sys

# # 숫자카드 개수 입력
# n = int(sys.stdin.readline())
# # 숫자카드 입력
# card = set(map(int, sys.stdin.readline().split()))

# # 확인할 숫자카드 개수 입력
# m = int(sys.stdin.readline())
# # 확인할 숫자카드 입력
# check = list(map(int, sys.stdin.readline().split()))

# # 딕셔너리 선언
# dic = {}
# # check에 있는 딕셔너리 0으로 초기화
# for c in check:
#     dic[c] = 0

# # print(dic)
# # cheack의 숫자가 card에 있으면 1 변경 
# for i in card:
#     if i in dic:
#         dic[i] = 1

# # dic의 값들 출력
# for d in dic:
#     print(dic[d], end=" ")

# ==========================================================
import sys
# 이진 탐색 라이브러리 추가
import bisect

# 숫자카드 개수 입력
n = int(sys.stdin.readline())
# 숫자카드 입력
card = list(map(int, sys.stdin.readline().split()))

# 확인할 숫자카드 개수 입력
m = int(sys.stdin.readline())
# 확인할 숫자카드 입력
check = list(map(int, sys.stdin.readline().split()))

# 이진 탐색은 정렬이 되어 있어야 함 
card.sort()

result = [0] * m

for c in check:
    # c가 처음 등장하는 위치(index)**를 반환
    l = bisect.bisect_left(card, c)
    # c가 마지막으로 등장한 다음 위치를 반환
    r = bisect.bisect_right(card, c)
    # c의 개수 확인
    print(r - l, end = ' ')
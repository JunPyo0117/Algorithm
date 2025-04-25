# 1초 초과/ 좀 느림 
import sys
import bisect

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))


n_list.sort()

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    # i가 처음 등장하는 위치(index)**를 반환
    l = bisect.bisect_left(n_list, i)
    # i가 마지막으로 등장한 다음 위치를 반환
    r = bisect.bisect_right(n_list, i)
    # i의 개수 확인
    print(r - l, end = ' ')

# ========================================================
# 딕셔너리 사용
import sys

# 숫자카드 개수 입력
n = int(sys.stdin.readline())
# 숫자카드 입력
card = list(map(int, sys.stdin.readline().split()))

# 확인할 숫자카드 개수 입력
m = int(sys.stdin.readline())
# 확인할 숫자카드 입력
check = list(map(int, sys.stdin.readline().split()))

# 딕셔너리 선언
dic = {}

# card에 있는 숫자를 카운트하면서 딕셔너리에 키/벨류로 저장 
for c in card:
    # 여러번 나오면 1씩 증가
    if c in dic:
        dic[c] +=1
    # 처음 나온 수 1 카운트 
    else:
        dic[c] = 1

# print(dic)

# check에 있는 숫자들 가져옴
for chk in check:
    # check에 있는 값이 dic에 있으면 dic의 값 출력 없으면 0 출력 
    if chk in dic:
        print(dic[chk], end=" ")
    else:
        print(0, end=" ")
from itertools import combinations  # 조합을 사용하기 위한 라이브러리

n, m = map(int, input().split())
data = list(map(int, input().split()))

max_sum = 0

combi = list(combinations(data, 3))
print(combi)

for combo in combinations(data, 3): # 조합을 사용, 순서 상관 없는 경우의 수를 나열
    total = sum(combo)
    if total <= m:
        max_sum = max(max_sum, total)

print(max_sum)

# ================================
# 브루트포스 알고리즘 
# 첫번째 카드는 n - 2까지의 선택이 가능하고, 
# 두번째 카드는 첫번째 카드를 제외한 후 n - 1까지의 선택이 가능
# 세번째 카드는 기선택된 첫번째 + 두번째 카드를 제외한 후 n까지의 선택이 가능
# 선택된 카드 3개의 합이 m을 넘지 않을 경우 기존의 max값과 비교하며 최댓값을 저장 후 출력

# import sys

# n, m = map(int, sys.stdin.readline().split())
# ret = 0
# card = list(map(int, sys.stdin.readline().split()))
# for i in range(n - 2):
# 	for j in range(i + 1, n - 1):
# 		for k in range(j + 1, n):
# 			if (card[i] + card[j] + card[k] <= m):
# 				ret = max(ret, card[i] + card[j] + card[k])
# print (ret)
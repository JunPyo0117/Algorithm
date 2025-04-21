import sys

input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    word = input().strip()
    arr.append(word)

set_word = list(set(arr))

# set_word.sort()          # 사전 순 정렬
# set_word.sort(key=len)   # 길이 순 정렬, 이미 사전 순으로 정렬 되어 있으므로 길이로 정렬해도 사전 순으로 유지
set_word.sort(key=lambda x: (len(x), x))  # key 설정을 통한 길이가 짧은 순으로 정렬 후 길이가 같으면 사전 순 정렬


for i in set_word:
    print(i)

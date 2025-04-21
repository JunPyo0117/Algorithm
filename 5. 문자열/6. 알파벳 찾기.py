s = input()


alpabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alpabet_cnt = [-1]*26

d = []

for i in s:
    for j in range(26):
        if i == alpabet[j]:
            d.append(j)

j = 0
for i in d:
    if alpabet_cnt[i] == -1: # 처음 등장한 위치만 기록 인덱스를 덮어쓰지 않기 위해
        alpabet_cnt[i] = j
    j += 1


for i in range(26):
    print(alpabet_cnt[i], end=' ')


# ======================================================================
# S = list(input())
# c = 'abcdefghijklmnopqrstuvwxyz'

# for i in c:
#     if i in S:
#         print(S.index(i), end =' ')
#     else:
#         print(-1, end=' ')

#=======================================================================
# S = input()

# for x in 'abcdefghijklmnopqrstuvwxyz':
#     print(S.find(x), end = ' ')
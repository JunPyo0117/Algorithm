# a_list = []

# for _ in range(5):
#     a_list.append(list(input()))


# b = ''

# for i in range(5):
#     b += a_list[i][0]
#     b += a_list[i][1]
#     for j in a_list[i]:
#         b += j[i]

# print(b)


# # ===================================

words = [input() for _ in range(5)]

result = ""

# 가장 긴 문자열의 길이 구하기
max_len = max(len(word) for word in words)

# 열 기준 탐색
for i in range(max_len):
    for j in range(5):
        if i < len(words[j]):
            result += words[j][i]

print(result)

# =====================================
words = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')
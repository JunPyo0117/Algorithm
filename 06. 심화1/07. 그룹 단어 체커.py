n = int(input())

d = []
cnt = 0
for _ in range(n):
    a = input()
    d.append(a)

result = []

for s in d:
    compressed = s[0]  # 첫 글자는 무조건 포함
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:  # 같으면 넘어감 
            compressed += s[i]  # 같지 않으면 해당 문자열 더하기 
    result.append(compressed) 

for i in range(len(result)):
    if len(result[i]) == len(set(result[i])):   # 중복된 문자가 없으면 cnt +1 
        cnt += 1

print(cnt)
# ==========================================================================
# N = int(input())
# count = 0

# for _ in range(N):
#   string = input()
#   if list(string) == sorted(string, key=string.find): # 문자의 처음 등장 순서대로 정렬한 것이 원래 문자 순서와 같다면 → 그룹 단어
#     count += 1

# print(count)
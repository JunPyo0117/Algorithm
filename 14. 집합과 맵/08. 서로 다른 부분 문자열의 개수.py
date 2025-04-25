import sys

# 문자열 S 입력
S = sys.stdin.readline().strip()

# print(S)
# 중복 제거를 위한 set
s = set()

# 모든 부분 문자열 생성
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        # set에 추가하여 자동으로 중복 제거
        s.add(S[i:j])

# 부분문자열 개수 출력
print(len(s))
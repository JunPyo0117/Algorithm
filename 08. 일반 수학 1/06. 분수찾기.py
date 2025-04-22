import sys

num = int(sys.stdin.readline())
line = 1


# 짝수 라인 : 분모가 1씩 늘어나고 분자가 1씩 줄어듦
# 홀수 라인 : 분자가 1씩 늘어나고 분모가 1씩 줄어듦

while num > line:
    num -= line
    line += 1

# 짝수일경우
if line % 2 == 0:
    a = num
    b = line - num + 1
# 홀수일경우
elif line % 2 == 1:
    a = line - num + 1
    b = num


print(str(a) + "/" + str(b))
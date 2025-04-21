# 이 방식은 시간이 너무 오래 걸림 실패 3초나 걸림

# import sys

# n = int(sys.stdin.readline())

# cnt = 0
# result = []

# for x in range(n):
#     for y in range(n):
#         if 3*x + 5*y == n:
#             result.append(x + y)

# if result == []:
#     print(-1)
# else:
#     print(min(result))

# ================================================
import sys

n = int(sys.stdin.readline())
cnt =0

while n >= 0:
    # 5로 나누어 떨어질 때 break
    if n % 5 == 0:
        cnt += n//5
        print(cnt)
        break

    # 3kg 봉투 한 개씩 빼기
    n -= 3
    cnt += 1

# 0으로 나누어 떨어지지 않을 시 -1을 출력
else:
    print(-1)
# # 소수 판별 함수
# def test(x):
#     if x < 2:
#         return False
#     for i in range(2, int(x**0.5)+1):
#         if x % i == 0:
#             return False
#     return True


# n = int(input())
# nums = list(map(int, input().split()))
# cnt = 0

# # 입력 받은 값을 소수 판별
# for num in nums:
#     if test(num):
#         cnt += 1

# print(cnt)

# ====================================================
n = int(input())
data = list(map(int, input().split()))
count = 0

for x in data:
    if x < 2:
        continue
    for i in range(2, x):  # 나눠지면 소수가 아님님
        if x % i == 0:
            break
    else:                  # 그 이외 소수
        count += 1

print(count)

# 내 풀이 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a, b = map(int, input().split())
# c = int(input())
# d = 0
# if b + c >= 60:
#     b2 = (b + c) % 60
#     d = (b + c) // 60 
#     if c >= 60:
#         if d >= 1:
#             a = (a + d)%24 
#         else:
#             a = (a + d)%24
#     else:
#         a = a + 1
#         if a >= 24:
#             a = a % 24
#         else:
#             a = a % 24
# else:
#     b2 = b + c
    

# print(a, b2)

# =========================================================
h, m = map(int, input().split())
t = int(input())

total_min = m + t
h += total_min // 60
m = total_min % 60

if h > 23:
    h-=24

print(h,m)
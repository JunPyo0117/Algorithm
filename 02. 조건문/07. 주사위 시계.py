# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.


a, b, c = map(int, input().split())

if a == b and a == c:
    print(10000+a*1000)
elif a == b or a == c or b == c:
    if a == b:
        print(1000+a*100)
    elif a == c:
        print(1000+a*100)
    else:
        b == c
        print(1000+b*100)
else:
    if a > b and a > c:
        print(a*100)
    elif b > a and b > c:
        print(b*100)
    else:
        print(c*100)

# a, b, c = map(int, input().split())
# if a == b == c:
#     print(10000 + a*1000)
# elif a == b or a == c:
#     print(1000 + a*100)
# elif b == c:
#     print(1000 + b*100)
# else:
#     print(max(a, b, c)*100)
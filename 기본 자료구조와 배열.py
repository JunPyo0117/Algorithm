# list01 = [1,2,3,4,5,6,7]

# for i in range(len(list01)//2):
#     list01[i], list01[len(list01)-i-1] = list01[len(list01)-i-1], list01[i]

# print(list01)

# =======================================================================
# x = ['A','B','C','D']

# for i, name in enumerate(x,1):
#     print(i, name)

# =======================================================================
def card_conv(x,r):
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r] # 해당하는 문자를 꺼내 결함
        x //= r

    return d[::-1] # 역순으로 변환

x = int(input())
r = int(input())

print(card_conv(x, r))
# =======================================================================
# 얇은 복사와 깊은 복사
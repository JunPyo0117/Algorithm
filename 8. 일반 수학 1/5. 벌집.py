n = int(input())

# 처음 방, 마지막 방 
a, b = 1, 1

while n > b:
    b += 6*a
    a += 1

print(a)
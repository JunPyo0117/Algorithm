arr = []

for _ in range(3):
    a = int(input())
    arr.append(a)

arr.sort()

if sum(arr) > 180 or sum(arr) < 180:
    print("Error")
elif arr[0] == 60 and arr[1] == 60 and arr[2] == 60:
    print("Equilateral")
elif arr[0] == arr[1] or arr[1] == arr[2]:
    print("Isosceles")
else:
    print("Scalene")

# ==================
a = int(input())
b = int(input())
c = int(input())

if a == b == c == 60:               # 세 각의 크기가 모두 60인 경우
    print("Equilateral")
elif a + b + c == 180:              # 세 각의 합이 180이고
    if a == b or b == c or c == a:  # 두 각이 같은 경우
        print("Isosceles")
    else:                           # 같은 각이 없는 경우
        print("Scalene")
else:                               # 세 각의 합이 180이 아닌 경우
    print("Error")
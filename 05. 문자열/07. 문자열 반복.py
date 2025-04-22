t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    print(''.join([ch * r for ch in s]))
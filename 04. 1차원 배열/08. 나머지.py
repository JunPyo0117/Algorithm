d = []
cnt = 0
for _ in range(10):
    a = int(input())
    d.append(a % 42)

print(len(set(d)))
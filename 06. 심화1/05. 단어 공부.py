a = input().upper()
list_a = list(set(a))

cnt = []

for i in list_a:
    count = a.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >1:
    print("?")
else:
    print(list_a[(cnt.index(max(cnt)))])
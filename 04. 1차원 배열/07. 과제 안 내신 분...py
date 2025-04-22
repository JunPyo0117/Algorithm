s = []
x = []
for _ in range(28):
    a = int(input())
    s.append(a)

for i in range(1, 31):
    if i not in s:
        x.append(i)

print(min(x))
print(max(x))

# student=[i for i in range(1,31)]
# for i in range(28):
#     data=int(input())
#     student.remove(data)
# print(min(student))
# print(max(student))
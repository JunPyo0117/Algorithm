n = int(input())
m = list(map(int, input().split()))

sum = 0

for i in range(len(m)):
    sum += m[i]/max(m)*100

print(sum/n)
m = int(input())
n = int(input())
prime_num = []


for x in range(m, n+1):
    if x < 2:
        continue  # 1 이하 스킵
    for i in range(2, x):  # 나눠지면 소수가 아님
        if x % i == 0:
            break
    else:                  # 그 이외 소수 
        prime_num.append(x)

if prime_num == []:
    print(-1)
else:
    print(sum(prime_num), min(prime_num), sep='\n')
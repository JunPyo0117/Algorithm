def test():
    n = int(input())
    arr = []
    i = 2
    
    while i*i <= n:
        if n % i == 0:
            arr.append(i)
            n //= i
        else:
            i += 1

    if n > 1:  # 마지막 남은 수가 1보다 크면 그것도 소인수
        arr.append(n)
    
    print('\n'.join(map(str, arr)))


test()

# =========================
def test():
    num = int(input())
    i = 2
    while num > 1:
        if num % i == 0:
            num = num // i
            print(i)
        else:
            i += 1

test()
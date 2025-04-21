def test():
    n, k = map(int, input().split())
    arr = []
    # 약수 배열 구하기 
    for i in range(1, n+1):
        if n % i == 0:
            arr.append(i)
            
    if len(arr) < k:
        print(0)
    else:
        print(arr[k-1])


test()
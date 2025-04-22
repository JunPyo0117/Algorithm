def test():
    while True:
        n = int(input())

        if n == -1:
            break
        
        arr = []
        # 약수 배열 구하기 
        for i in range(1, n):
            if n % i == 0:
                arr.append(i)
        if n == sum(arr):
            print(n, "=", ' + '.join(map(str, arr)))
        else:
            print(n, "is NOT perfect.")


test()

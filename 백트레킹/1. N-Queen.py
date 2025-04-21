import sys
# 아 진짜 모르겠다 재귀 너무 어렵다/ fork 연습하기
n = int(sys.stdin.readline())

result = [0]
chk = [False] * (n+1)


def recursive(row):
    cnt = 0
    if row == n:
        cnt += 1
        print(''.join(map(str, result)))
        return

    for col in range(1, n+1):
         if chk[i] == False:
            chk[i] = True
            result.append(i)
            recursive(row+1)
            chk[i] = False
            result.pop()            

recursive(0)


# print(board)


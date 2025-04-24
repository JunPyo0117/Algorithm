# 빠른 입력을 받기 위한 라이브러리 임포트
import sys
# input 함수 재정의
input = sys.stdin.readline

# 보드의 크기 입력  
n, m = map(int, input().split())
# 보드 입력
board = [input().strip() for _ in range(n)]
# 결과 저장 리스트
result = []

# 8x8 체스판 탐색  n-7, m-7은 8x8 체스판 선정
for i in range(n-7):
    for j in range(m-7):
        # 첫 번째 체스판 탐색   
        index1 = 0
        # 두 번째 체스판 탐색
        index2 = 0
        # 8x8 체스판 탐색
        for k in range(i, i+8):
            for l in range(j, j+8):
                # 첫 번째 체스판 탐색
                if (k+l) % 2 == 0:
                    if board[k][l] == 'W':
                        index1 += 1
                    else:
                        index2 += 1
                # 두 번째 체스판 탐색
                else:
                    if board[k][l] == 'W':
                        index2 += 1
                    else:
                        index1 += 1
        # 첫 번째 체스판과 두 번째 체스판 중 최소 개수 저장
        result.append(min(index1, index2))
# 결과 출력 
print(min(result))





# 빠른 입력을 받기 위한 라이브러리 임포트
import sys

n = int(sys.stdin.readline())

# 종말 년도 초기화
end_year = 666
# 종말 년도 개수 초기화
cnt = 0

# 종말 년도 개수가 n이 될 때까지 반복
while True:
    # 종말 년도에 666이 포함되어 있으면 종말 년도 개수 증가
    if '666' in str(end_year):
        cnt += 1
    # 종말 년도 개수가 n이 되면 반복문 종료
    if cnt == n:
        break

    end_year += 1
    print(end_year)    
    
# 종말 년도 출력
print(end_year)
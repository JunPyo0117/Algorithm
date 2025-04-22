import sys

n = int(sys.stdin.readline())

end_year = 666

cnt = 0

while True:
    if '666' in str(end_year):
        cnt += 1

    if cnt == n:
        break

    end_year += 1    
    

print(end_year)
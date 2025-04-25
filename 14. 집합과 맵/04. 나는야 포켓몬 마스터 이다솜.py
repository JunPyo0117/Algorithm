import sys

n, m = map(int, sys.stdin.readline().split())
dic_name = {}
dic_num = {}

for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    dic_name[i] = name
    dic_num[name] = i

# print(dic)

for _ in range(m):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        question = int(question)
        print(dic_name[question])
    else:
        print(dic_num[question])

    



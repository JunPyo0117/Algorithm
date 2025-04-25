import sys

n = int(sys.stdin.readline())

log_set = set()

for _ in range(n):
    name, log = sys.stdin.readline().split()
    if log == "enter":
        log_set.add(name)
    elif log == "leave":
        log_set.discard(name)  # remove도 가능하지만 discard는 없으면 에러 안 남

# 역순으로 정렬해서 출력
for name in sorted(log_set, reverse=True):
    print(name)

# ===========================================================
import sys

n = int(sys.stdin.readline())
dic = {}

for _ in range(n):
    name, log = sys.stdin.readline().split()
    dic[name] = log
    if log == "leave":
        del dic[name]

d = sorted(dic.items(), reverse=True)
dic = dict(d)

for key in dic.keys():
    print(key)

# ===============================================================
# # 시간 초과~~~~~~~~~~~~~
# import sys

# n = int(sys.stdin.readline())

# dic = {}
# for _ in range(n):
#     name, log = sys.stdin.readline().split()
#     dic[name] = log

# name_list = []
# for key, value in dic.items():
#     if value == "enter":
#         name_list.append(key)
#         reversed_name = sorted(name_list, reverse=True)

# print("\".join(map(str, reversed_name)))
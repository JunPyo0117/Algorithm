dic = {"c=": "č", "c-": "ć", "dz=": "dž", "d-": "đ", "lj": "lj", "nj": "nj", "s=": "š", "z=": "ž"}

a = input()

cnt = 0

d = []

for k, v in dic.items():
    cnt = a.count(k)
    d.extend([k] * cnt)

print(len(a)-len(d))

#==================================================
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()

# for i in croatia :
#     word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
# print(len(word))
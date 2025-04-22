grade = {"A+": 4.5, "A0": 4.0,
         "B+": 3.5, "B0": 3.0,
         "C+": 2.5, "C0": 2.0,
         "D+": 1.5, "D0": 1.0,
         "F": 0.0}

c_g_list = []
c_list = []

for _ in range(20):
    sub, c, g = input().split()
    if g == "P":
        continue
    score = grade[g]
    c_g_list.append(float(c)*score)
    c_list.append(float(c))


print(sum(c_g_list)/sum(c_list))

# ===========================================================
# ul = ["A+","A0","B+","B0","C+","C0","D+","D0","F"]
# u = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]

# s = 0
# unit_sum = 0 
# for i in range(20):
#     a,b,c = input().split()
#     b = float(b)
    
#     if(c!="P"):
#         s += u[ul.index(c)]*b
#         unit_sum += b

# print(f'{s / unit_sum:.6f}')

#=====================================================
# score = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0}

# s = 0
# t = 0

# for i in range(20):
#   a, b, c = input().split()
#   b = float(b)
#   if c == "P":
#     continue
#   else:
#     s = s + score[c] * b
#   t = t + b

# s = s / t
# print(s)
a = input()

arry = [0, 0, 1, "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

d = []

for i in a:
    for j in range(len(arry)):
        if i in str(arry[j]):
            d.append(j)

print(sum(d))

# =====================================================================
# word = input()
# arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# result = 0
 
# for str in word:
#     for i in arr:
#         if str in i:
#             result += arr.index(i) + 3
#             break
 
# print(result)
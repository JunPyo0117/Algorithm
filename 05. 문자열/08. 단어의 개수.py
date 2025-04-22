s = input()

if s == " ":
    cnt = 0
elif s[0] == " " and s[-1] == " ":
    cnt = -1
    for i in s:
        if i == " ":
            cnt += 1
elif s[0] == " " or s[-1] == " ":
    cnt = 0
    for i in s:
        if i == " ":
            cnt += 1
else:
    cnt = 1
    for i in s:
        if i == " ":
            cnt += 1
    
print(cnt)


# ===========================
# string = input().split()

# print(len(string))

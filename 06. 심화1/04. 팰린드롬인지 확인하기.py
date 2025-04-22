a = input()

if a == ''.join(reversed(a)):
    print(1)
else:
    print(0)
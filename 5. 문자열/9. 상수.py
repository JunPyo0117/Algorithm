a, b = input().split()

# a = a[::-1]
# b = b[::-1]

a = reversed(a)
b = reversed(b)

print(max(''.join(a), ''.join(b)))
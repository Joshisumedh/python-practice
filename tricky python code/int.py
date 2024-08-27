# Convert a string to int without using built-in int()

str_input = input()

l = []
ans = 0

for i in str_input:
    l.append(ord(i) - ord('0'))  

length = len(l)
mask = [10**i for i in reversed(range(length))]

for i in range(length):
    ans += l[i] * mask[i]

print(ans)
print(type(ans))
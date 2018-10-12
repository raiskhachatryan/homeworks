n = int(input("input index "))
lst = []
a, b = 0, 1
for i in range(n+1):
    lst.append(b)
    a, b = b, a + b

print(i, "index is", lst[i])



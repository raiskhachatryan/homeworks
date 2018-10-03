a = []

for i in range(4):
    for j in [[0]*4]:
        a.append(j)
# print(a)
for i in range(4):
    for j in range(4):
        if a[i] == a[j]:
            a[i][j] = 1
        else:
            a[i][j] = 2
print(a)






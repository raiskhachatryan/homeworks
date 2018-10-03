list1 = [3, 6, True, True, -1, "abc", (1, 2), [2, 3], 6]
index = 0
for i in range(len(list1)):
    if type(list1[i]) == tuple:
        print(index, list1[i])
        break
    index += 1



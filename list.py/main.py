li = [1, 46, 3, 88]
print(li)

li.append("5")  # li = [1,2,46,88,5]
li.reverse()  # print -> reverse
li.sort()  # li = [1, 3, 46, 88]
li.insert(2, '5')  # li = [1, 3, 5, 46, 88]
li.remove('3')  # li = [1, 46, 88]

item = li.pop()  # item = 88, li = [1, 46, 3]

li2 = [4, 6, 8]
li.extend(li2)  # li = [1, 46, 3, 88, 4, 6, 8]

li.count(0)  # 1

del(li[0])  # li = [46, 3, 88]

lis = li + li2  # li = [1, 46, 3, 88, 4, 6, 8]


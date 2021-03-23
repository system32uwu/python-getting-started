myList:list[int] = [1,2,3]

myList.append(4)
myList.append(5)
myList.append(6)

for item in myList:
    print("Item: {}".format(item))

#Use enumerate when you want to extract the index as well.
for index,item in enumerate(myList):
    print("Index: {} Item: {}".format(index,item))
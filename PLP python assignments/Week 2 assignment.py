#creating an empty list
mylist = []
mylist.append(10)
mylist.append(20)
mylist.append(30)
mylist.append(40)
print(mylist)
mylist.insert(1,15) 
print(mylist)
mylist2 = [50,60,70]
mylist.extend(mylist2)
print(mylist)
mylist.pop()
print(mylist)
mylist.sort()
print(mylist)
index30 = mylist.index(30)
print(index30)

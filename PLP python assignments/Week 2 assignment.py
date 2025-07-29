#creating an empty list
mylist = []
#append 10,20,30,40
mylist.append(10)
mylist.append(20)
mylist.append(30)
mylist.append(40)
print(mylist)
#inserting 15 at the second position, first index
mylist.insert(1,15) 
print(mylist)
#creating a new list and extending the initial one with the new one
mylist2 = [50,60,70]
mylist.extend(mylist2)
print(mylist)
#deleting the last item
mylist.pop()
print(mylist)
#sorting in an ascending order
mylist.sort()
print(mylist)
#printing the index of 30 on the list
index30 = mylist.index(30)
print(index30)

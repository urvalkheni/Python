countires = ("Spain","Italy","India","England","Germany")
print(countires)
temp = list(countires)
temp.append("Japan") # add item
temp.pop(3) # remove item
temp[3] = "America" # change item
countires = tuple(temp)
print(countires)
tuple1 = (0,0,0,7,1,2,3,4,4,5,6,6,7,7,7)
res = tuple1.count(4)
print("Count of 4 in tuple1 is ::",res)
res = tuple1.index(7)
print("index of 7 in tuple1 is ::",res)
res = tuple1.index(7,4,13) # slicing and than find index of element
print("index of 7 in tuple1 is ::",res)
res = len(tuple1)
print("The Length of the tuple is ::",res)
# you cna't change the tuple but you can convert it in list and than 
# do chnages and than make it tuple 
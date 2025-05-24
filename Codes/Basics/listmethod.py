l = [4,3,1,2,1,1,2,3,4,8]
print(l)
l.append(5) # this is use to add element at the last
print(l)
l.reverse() # this will reverse the order of the list
print(l) 
l.sort() # sort list in ascending order
print(l)
l.sort(reverse=True) # sort in decending order
print(l)
print(l.index(1)) # give the index of the first occurens
print(l.count(1)) # give how many time the 1 vomes in list
print(l)
# m=l if you do somthing like this it will take reference of l 
# so chnages in m lead to chnage in m so avoid this type of 
# thing in the pyhton
# m[0] = 0
# print(l)
m = l.copy() # this will make copy and don't affect the l
m[0] = 0
print(l) 

l.insert(1,777)
print(l)

m = [900,100,1100]
k = m + l
l.extend(m) # joint two list
print(l)
print(k)
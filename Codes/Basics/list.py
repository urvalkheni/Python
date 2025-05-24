#list is order format of data enclose by square brackets 
#one list have multiple type of data collection
l = [3,5,6,"Urval",True,7,8,9,1,2,3]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[-3]) #negative index
print(l[len(l)-3]) # become positive index

if "Urval" in l:
    print("Yes")
else:
    print("No")
if "val" in "Urval":
    print("Yes it is")
else:
    print("No it's not")
print(l)
print(l[:])
print(l[:len(l):2])
#List Comprehension
lst = [(i+1)*(i+1) for i in range(10)]
print(lst)
lst = [(i+2)*(i+2) for i in range(11) if(i%2==0)]
print(lst)
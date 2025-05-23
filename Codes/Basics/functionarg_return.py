# avg(6,9)
#defualt Arguments
def avg1(a=9,b=1):
    print("The average of",a,"and",b,"is ::",(a+b)/2)
avg1()
avg1(5,3)
avg1(2)

#keyword Arguments
avg1(b=10,a=20) # don't care about orede

#Requierd Arguments
def avg2(a,b=1):
    print("The average of",a,"and",b,"is ::",(a+b)/2)
# avg2() this will show error cuz you have to provide the value of a is must
avg2(5) # here if you don't give b it will ohky it will not thor error

#variable length Arguments
def avg3(*n):
    sum = 0
    for i in n:
        sum += i
    print("The Average is ::",sum/len(n))
avg3(1,2,3,4,5,6,7,8,9,10)

def name(**name):
    print("Currently out of concept")
    print(type(name))
    print("Hello,",name["fname"],name["mname"],name["lname"])

name(lname="Hiteshbhai",fname="Kheni",mname="Urval")

#return type
def avg4(*n):
    sum = 0
    for i in n:
        sum += i
    return sum/len(n) # return the value to the function
c = avg4(1,2,3,4,5,6,7,8,9,10)
print("The Average is ::",c)
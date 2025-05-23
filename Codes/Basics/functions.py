def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean) 
def NumBehave(a,b):
    if(a>b):
        print("First Number",a,"is Greater")
    elif(b>a):
        print("Second Number",b,"is Greater")
    else:
        print("Both Numbers are Equal")
   
num1 = int(input("Enter The First Number :: "))
num2 = int(input("Enter The Second Number :: "))
NumBehave(num1,num2)
calculateGmean(num1,num2)
# you can make function to reuse your code
# a = 4
# b = 2
# gmean1 = (a*b)/(a+b)
# print(gmean1)
# c = 8
# d = 6
# gmean2 = (a*b)/(a+b)
# print(gmean2)
'''
1. Built in function
    built in python
2. User Define function
    built by user
make sure of indent in userdefine function
'''
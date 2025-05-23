num1 = int(input("Enter The First Number :: "))
num2 = int(input("Enter The Second Number :: "))
num3 = int(input("Enter The Third Number :: "))
num4 = int(input("Enter The Fourth Number :: "))
def max(a,b,c,d):
    if(a==b==c==d):
        print("Num1 ::",a,"Num2 ::",b,"Num3 ::",c,"Num4 ::",d,"All are equal.")
    elif(a>b):
        if(a>c):
            if(a>d):
                print("Num1",a,"is largest.")
    elif(b>c):
        if(b>d):
            print("Num2 ",b,"is largest")
    elif(c>d):
        print("Num3",c,"is largest.")
    else:
        print("Num4",d,"is largest.")
max(num1,num2,num3,num3)
a = int(input("Enter The First Number :: "))
b = int(input("Enter The Second Number :: "))
c = int(input("Enter The Third Number :: "))
if(a>b):
    if(a>c):
        print("First Number is Greter than both")
    elif(a>10):
        print("It is Greater than 10")
    else:
        print("First Number is Just Greter than Second Number")
else:
    if(b>c):
        print("second Number is most big")
    elif(b>10):
        print("It is Greater than 10")
    else:
        print("The Third Number is most big")
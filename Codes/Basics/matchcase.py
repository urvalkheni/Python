x = int(input("Enter The Value of x :: "))
# x is the variable to match
match x:
    #if x is 0
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x)
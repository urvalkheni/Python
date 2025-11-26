#This is The Program of Automorphic Number from m to n
#An Automorphic Number is a number whose square ends with the same digits as the number itself.
start_number = int(input("Enter start number: "))
end_number = int(input("Enter end number: "))
for i in range(start_number, end_number + 1):
    squared = i ** 2
    if str(squared).endswith(str(i)):
        print(f"{i} is an Automorphic Number and its square is {squared}")
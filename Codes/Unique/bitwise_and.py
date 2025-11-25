#using bitwise operators to find number is even or odd

first_number = int(input("Enter an integer: "))

# Check if the number is even or odd using bitwise AND operator
if first_number & 1:
    print(f"{first_number} is an odd number.")
else:
    print(f"{first_number} is an even number.")
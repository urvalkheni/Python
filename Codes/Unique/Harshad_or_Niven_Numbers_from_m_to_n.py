#Harshad or Niven Number from m to 
#This is the number is which is divisible by the sum of thier didgits.
#Example: 18 → 1 + 8 = 9 and 18 is divisible by 9 = 2
number_start = int(input("Enter start number: "))
number_end = int(input("Enter end number: "))
for num in range(number_start, number_end + 1):
    sum_of_digits = sum(int(digit) for digit in str(num))
    if num % sum_of_digits == 0:
        print(f"{num} is a Harshad or Niven Number") 
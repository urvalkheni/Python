# Strong Number
# Sum of factorials of the digits = number.
# Example: 145 → 1! + 4! + 5! = 145
import math
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
strong_numbers = []
def is_strong(num):
    return num == sum(math.factorial(int(digit)) for digit in str(num))
for num in range(start, end + 1):
    if is_strong(num):
        strong_numbers.append(num)
if strong_numbers:
    print("Strong numbers between", start, "and", end, "are:", ' '.join(map(str, strong_numbers)))
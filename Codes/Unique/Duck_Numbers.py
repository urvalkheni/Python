# Duck Number
# Number containing zero(s) but not starting with zero.
# Example: 204, 1030
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
duck_numbers = []
def is_duck(num):
    num_str = str(num)
    return '0' in num_str[1:]  # Check for '0' in the number excluding the first digit
for num in range(start, end + 1):
    if is_duck(num):
        duck_numbers.append(num)
if duck_numbers:
    print("Duck numbers between", start, "and", end, "are:", ' '.join(map(str, duck_numbers)))
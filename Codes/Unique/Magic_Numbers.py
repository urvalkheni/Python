# Magic Number

# Repeated digit sum becomes 1.
# Example: 1729 → 1+7+2+9 = 19 → 1+9 = 10 → 1+0 = 1
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
magic_numbers = []
def is_magic(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num == 1
for num in range(start, end + 1):
    if is_magic(num):
        magic_numbers.append(num)
if magic_numbers:
    print("Magic numbers between", start, "and", end, "are:", ' '.join(map(str, magic_numbers)))
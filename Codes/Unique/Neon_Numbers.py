# Neon Number
# Sum of digits of its square equals the number.
# Example: 9 → 9² = 81 → 8+1 = 9
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
neon_numbers = []
for num in range(start, end + 1):
    squared_num = num ** 2
    digit_sum = sum(int(digit) for digit in str(squared_num))
    if digit_sum == num:
        neon_numbers.append(num)
if neon_numbers:
    print("Neon numbers between", start, "and", end, "are:", ' '.join(map(str, neon_numbers)))
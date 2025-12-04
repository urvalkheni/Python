# Spy Number
# Sum of digits = product of digits
# Example: 123 → sum = 1+2+3 = 6, product = 1×2×3 = 6 → spy
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
spy_numbers = []
def is_spy(num):
    digits = [int(digit) for digit in str(num)]
    digit_sum = sum(digits)
    digit_product = 1
    for digit in digits:
        digit_product *= digit
    return digit_sum == digit_product
for num in range(start, end + 1):
    if is_spy(num):
        spy_numbers.append(num)
if spy_numbers:
    print("Spy numbers between", start, "and", end, "are:", ' '.join(map(str, spy_numbers)))
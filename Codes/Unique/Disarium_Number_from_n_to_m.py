# Disarium Number from n to m
# Sum of digits powered by their position equals the number.
# Example: 135 → 1¹ + 3² + 5³ = 135
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
for number in range(start, end + 1):
    sum_of_powers = 0
    digits = str(number)
    for index, digit in enumerate(digits):
        sum_of_powers += int(digit) ** (index + 1)
    if sum_of_powers == number:
        print(f"{number} is a Disarium Number")
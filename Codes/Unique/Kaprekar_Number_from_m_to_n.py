# Kaprekar Number
# Square the number → split → sum = original number.
# Example: 45 → 2025 → 20 + 25 = 45
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
kaprekar_numbers = []
for num in range(start, end + 1):
    squared_num = str(num ** 2)
    d = len(str(num))
    right_part = squared_num[-d:] if d <= len(squared_num) else squared_num
    left_part = squared_num[:-d] if d < len(squared_num) else '0'
    if int(left_part) + int(right_part) == num:
        kaprekar_numbers.append(num)
if kaprekar_numbers:
    print("Kaprekar numbers between", start, "and", end, "are:", ' '.join(map(str, kaprekar_numbers)))
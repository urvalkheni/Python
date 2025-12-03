#Happy Number
#Repeated sum of squares of digits → ends at 1
#Example: 19 → 1²+9²=82 → 8²+2²=68 → … → 1
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
happy_numbers = []
def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1
for num in range(start, end + 1):
    if is_happy(num):
        happy_numbers.append(num)
if happy_numbers:
    print("Happy numbers between", start, "and", end, "are:", ' '.join(map(str, happy_numbers)))

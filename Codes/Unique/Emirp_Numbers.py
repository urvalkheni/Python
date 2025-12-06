# Emirp Number
# Prime number that becomes a different prime when reversed.
# Example: 13 → reverse 31 (both prime)
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
emirp_numbers = []
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def is_emirp(num):
    if not is_prime(num):
        return False
    reversed_num = int(str(num)[::-1])
    return reversed_num != num and is_prime(reversed_num)
for num in range(start, end + 1):
    if is_emirp(num):
        emirp_numbers.append(num)
if emirp_numbers:
    print("Emirp numbers between", start, "and", end, "are:", ' '.join(map(str, emirp_numbers)))
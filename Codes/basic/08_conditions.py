"""08_conditions.py
if/elif/else, comparisons, logical operators.
"""

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C or below"
print("Grade:", grade)

x = 5
print(x > 3, x < 10, x == 5, x != 2, x >= 5, x <= 5)

is_member = True
has_coupon = False
discount = is_member and not has_coupon
print("Discount applied?", discount)

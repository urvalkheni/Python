"""11_lists.py
List indexing, slicing, methods, iteration.
"""

nums = [10, 20, 30, 40]
print(nums[0], nums[-1])
print(nums[1:3])
print(nums[:2])
print(nums[2:])

nums.append(50)
nums.insert(1, 15)
removed = nums.pop()
nums.remove(30)
print("Removed last:", removed)
print("List now:", nums)

for n in nums:
    print("Item:", n)

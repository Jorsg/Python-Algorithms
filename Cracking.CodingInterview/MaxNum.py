# Find the maximum number in a list of numbers
def max_num(nums: list[int]) -> int:
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

# Test cases
print(max_num([1, 2, 3, 4, 5])) # 5
print(max_num([10, 4, 3, 2, 1])) # 10
print(max_num([1, 1, 1, 1, 1])) # 1

# Time complexity: O(n)

# Space complexity: O(1)

def max_num1(nums: list[int]) -> int:
    num_max = nums[0]
    for num in nums:
        if num_max < num:
            num_max = num
    return num_max

# Test cases
print(max_num1([1, 2, 3, 4, 5])) # 5

# Time complexity: O(n)

# Space complexity: O(1)
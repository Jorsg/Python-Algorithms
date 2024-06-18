def find_integer_added(num1, num2):

   sum_diff = sum(num2[i] - num1[i] for i in range(len(num1)))

   x = sum_diff // len(num1)

   return x



# Example usage
nums1_example1 = [2, 6, 4]
nums2_example1 = [9, 7, 5]

nums1_example2 = [10]
nums2_example2 = [5]

nums1_example3 = [1, 1, 1, 1]
nums2_example3 = [1, 1, 1, 1]
print(find_integer_added(nums1_example1, nums2_example1))  # Output: 3
print(find_integer_added(nums1_example2, nums2_example2))  # Output: -5
print(find_integer_added(nums1_example3, nums2_example3))  # Output: 0
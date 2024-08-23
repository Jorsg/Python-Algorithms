# 3162. Find the Number of Good Pairs I
#Given two arrays of integers nums1 and nums2, return the number of pairs (i, j) such that i < j and nums1[i] * k == nums2[j].
#A pair(i, j) is called good if there are no other good pairs(i1, j1) where i1 < j1 and nums1[i1] * k == nums2[j1].
#Example 1:
#Input: nums1 = [1, 2, 2, 4], nums2 = [2, 2], k = 2
#Output: 2
#Explanation: There are two good pairs(0, 1) and(0, 2).

def number_Of_Pairs(nums1, nums2, k):
    result = 0
    for num1 in nums1:
        for num2 in nums2:
            if num1 %(num2 * k) == 0:
             result += 1

    return result



print(number_Of_Pairs([1, 2, 2, 4],  [2, 2], 2))


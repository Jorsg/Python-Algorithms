# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
# EXAMPLE
# Input: "abc", "bca"
# Output: True
# Time complexity: O(n)
def check_permutation(string1, string2):
    #If the strings are different lengths, they cannot be permutations
    if len(string1) != len(string2):
        return False
    #Create a dictionary to store the frequency of each character in string1
    char_count = {}
    for char in string1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    #Iterate through string2
    for char in string2:
        #If the character is not in the dictionary, return False
        if char not in char_count:
            return False
        #If the character is in the dictionary, decrement the count
        char_count[char] -= 1
        #If the count is less than 0, return False
        if char_count[char] < 0:
            return False
    return True
# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same
# forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. You can ignore casing
# and no-letter characters.
# EXAMPLE
# input: Tact Coa
# Output: True(permutation: "taco cat", "atco cta")

from collections import Counter

def is_palindrome_permutation(s):
    s= ''.join(c.lower() for c in s if c.isalpha())

    char_counts = Counter(s)

    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)

    return odd_count <= 1


print(is_palindrome_permutation("Tact Coa"))    

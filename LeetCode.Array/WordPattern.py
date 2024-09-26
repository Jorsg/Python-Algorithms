#290. Word Pattern
#Given a pattern and a string s, find if s follows the same pattern.
#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
#Example 1:
#Input: pattern = "abba", s = "dog cat cat dog"
#Output: true
#Example 2:
#Input: pattern = "abba", s = "dog cat cat fish"
#Output: false

def word_pattern(pattern, s):
    words = s.split()

    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for char, words in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != words:
                return False
        else:
            if words in word_to_char:
                return False

            char_to_word[char] = words
            word_to_char[words] = char

    return True 


# Ejemplos de uso
print(word_pattern("abba", "dog cat cat dog"))  # True
print(word_pattern("abba", "dog cat cat fish")) # False
print(word_pattern("aaaa", "dog cat cat dog"))  # False    

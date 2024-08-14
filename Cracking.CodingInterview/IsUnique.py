#Create algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
#Time complexity: O(n)
def is_unique(string):
    #If the string is longer than the number of unique characters, it must have duplicates
    if len(string) > 128:
        return False
    #Create an array of boolean values to represent each character
    char_set = [False] * 128
    for char in string:
        #If the character has been seen before, return False
        if char_set[ord(char)]:
            return False
        #Otherwise, mark the character as seen
        char_set[ord(char)] = True
    return True
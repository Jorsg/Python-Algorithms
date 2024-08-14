# 1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"
# Time complexity: O(n)
def urlify(string, length):
    #Convert the string to a list of characters
    string = list(string)
    #Create a pointer to the end of the string
    end = len(string)
    #Iterate through the string
    for i in range(length - 1, -1, -1):
        #If the character is not a space, move it to the end of the string
        if string[i] != ' ':
            string[end - 1] = string[i]
            end -= 1
        #If the character is a space, replace it with '%20'
        else:
            string[end - 3:end] = '%20'
            end -= 3
    return ''.join(string)
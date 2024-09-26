#1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another.
#Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
#Time complexity: O(n)
#Space complexity: O(n)
#s1 = xy = waterbottle
#x = wat
#y = erbottle
#s2 = yx = erbottlewat
#s2 will always be a substring of s1s1
#s1s1 = xyxy = waterbottlewaterbottle
#s2 = yx = erbottlewat
#s1s1 contains s2
#s2 is a rotation of s1

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    newstring = s1 + s1
    return s2 in newstring

# Ejemplos de uso
print(is_rotation("waterbottle", "erbottlewat"))  # True
print(is_rotation("hello", "llohe"))              # True
print(is_rotation("python", "nytho"))             # False    
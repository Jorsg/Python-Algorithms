# 242. Valid Anagram 
# Given two string s and t, return true if t is an anagram of s,  and false  otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Paso 1: Verificar si las longitudes son iguales
        if len(s) != len(t):
            return False

        # Paso 2: Crear un diccionario para contar la frecuencia de caracteres en s
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Pasos 3 y 4: Recorrer t y actualizar el diccionario
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False

        # Paso 5: Si llegamos aquí, las cadenas son anagramas
        return True

# Ejemplo de uso
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Debería imprimir: True
print(solution.isAnagram("rat", "car"))  # Debería imprimir: False







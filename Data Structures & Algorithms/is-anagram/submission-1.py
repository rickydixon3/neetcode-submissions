class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        str_s = {}
        str_t = {}

        for char in s:
            if char in str_s:
                str_s[char]+= 1
            else:
                str_s[char] = 1

        for char in t:
            if char in str_t:
                str_t[char] += 1
            else:
                str_t[char] = 1

        return str_s == str_t

        









        
class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleanStr = ""

        # Getting our string
        for char in s:
            if char.isalnum():
                cleanStr += char.lower()

        left = 0
        right = len(cleanStr) - 1

        while left < right:
            if cleanStr[left] != cleanStr[right]:
                return False
            left += 1
            right -= 1

        return True


        
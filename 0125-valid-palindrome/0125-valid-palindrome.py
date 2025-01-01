class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c
        i = 0
        j = len(clean) - 1
        while i < j:
            if clean[i] != clean[j]:
                return False
            i += 1
            j -= 1
        return True

        
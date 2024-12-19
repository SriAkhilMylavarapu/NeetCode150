class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphalists = [0]*26
        alphalistt = [0]*26
        for c in s:
            alphalists[ord(c)-ord('a')] += 1
        for c in t:
            alphalistt[ord(c)-ord('a')] += 1
        if alphalistt == alphalists:
            return True
        return False
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        maxl = 0
        for n in nums:
            if n-1 not in setnums:
                l = 0
                while (n + l) in setnums:
                    l += 1
                maxl = max(maxl, l)
        return maxl

        
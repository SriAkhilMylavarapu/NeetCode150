class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxa =  min(height[l], height[r]) * (r-l)

        while l < r:
            maxa = max(maxa, min(height[l], height[r]) * (r-l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return maxa
        
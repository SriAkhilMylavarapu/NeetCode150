class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxa =  min(height[l], height[r]) * (r-l)

        while l < r:
            if height[l] < height[r]:
                l += 1
            maxa = max(maxa, min(height[l], height[r]) * (r-l))
            if height[r] < height[l]:
                r -= 1
            maxa = max(maxa, min(height[l], height[r]) * (r-l))
            if height[l] == height[r] and l < r:
                if height[l+1] >= height[r-1]:
                    l += 1
                else:
                    r -= 1

        return maxa
        
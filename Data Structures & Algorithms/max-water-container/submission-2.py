class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxVol = 0

        # 1,7,2,5,12,3,500,500,7,8,4,7,3,6

        while left < right:
            if heights[left] < heights[right]:
                lvol = min(heights[left], heights[right]) * (right-left)
                maxVol = max(lvol, maxVol)
                left += 1
            elif heights[left] >= heights[right]:
                lvol = min(heights[left], heights[right]) * (right-left)
                maxVol = max(lvol, maxVol)
                right -= 1
        
        return maxVol
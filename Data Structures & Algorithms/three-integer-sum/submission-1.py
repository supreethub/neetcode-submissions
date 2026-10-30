class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        left, right = 0, len(nums) - 1
        res = []

        # [-4, -1, -1, 0, 1, 2]

        for idx, a in enumerate(nums):
            if idx > 0 and a == nums[idx - 1]:
                continue
            
            left, right = idx+1, len(nums) - 1
            while left < right:
                tsum = a + nums[left] + nums[right]
                if tsum > 0:
                    right -= 1
                elif tsum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
                
            
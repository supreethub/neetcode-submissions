class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap w/ diff checks?
        hmap = {} # diff, val

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hmap:
                return [hmap[diff], i]
            hmap[num] = i




        


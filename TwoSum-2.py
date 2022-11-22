from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        map = {}
        for i in range(n):
            x = target - nums[i]
            if x in map:
                return[map[x], i]
            map[nums[i]] = i
        return 0



solu = Solution()
nums = [2,7,11,15]
print(solu.twoSum(nums,target=9))
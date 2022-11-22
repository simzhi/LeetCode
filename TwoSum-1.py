from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return[i,j]



solu = Solution()
nums = [2,7,11,15]
print(solu.twoSum(nums,target=9))
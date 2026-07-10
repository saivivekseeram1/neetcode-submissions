class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for left in range(n):
            for right in range(left + 1, n):
                sum=nums[left]+nums[right]
                if sum==target:
                    return [left,right]
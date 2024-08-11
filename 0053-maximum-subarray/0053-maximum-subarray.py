class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = nums[0]
        max_global = nums[0]
        for num in nums[1:]:
            if max_current + num > num :
                max_current = max_current + num
            else:
                max_current = num
            
            if max_current > max_global :
                max_global = max_current
        return (max_global)
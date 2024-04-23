class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zeroth_index = 0
        for zeroth_index in range(0, len(nums)):
            if nums[zeroth_index] != 0 :
                # Swapping both numbers without x, y = y,x
                temp = nums[non_zeroth_index]
                nums[non_zeroth_index] = nums[zeroth_index]
                nums[zeroth_index] = temp
                # Iterating the zeroth_index by 1
                non_zeroth_index += 1
        

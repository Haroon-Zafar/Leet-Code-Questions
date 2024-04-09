class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Initiating an dictionary which will contain the indices of the two sum elements 
        # This index_array will be returned
        nums_with_indices_dict = {}

        for i in range(0, len(nums)):
            num = nums[i]
            # nums is the original list
            # complement = target - num[i]
            complement = target - num
            if complement in nums_with_indices_dict:
                return(nums_with_indices_dict[complement], i)
            nums_with_indices_dict[num] = i
            
            

        
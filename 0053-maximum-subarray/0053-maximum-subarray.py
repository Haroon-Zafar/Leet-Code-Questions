class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # using kadane' algorithm
        # current_sum = nums[0]
        # maximum_sum = nums[0]

        # # If there is only a single element in the list
        # if len(nums) == 1 :
        #     return(nums[0])
        
        # for index in range(1, len(nums)):

        #     # if sum is negative
        #     if current_sum < 0 :
        #         current_sum = nums[index]
            
        #     # if sum is positive 
        #     else : 
        #         current_sum += nums[index]
            
        #     if current_sum > maximum_sum : 
        #         # update the maximum_sum 
        #         maximum_sum = current_sum
        # return (maximum_sum)

        max_current = max_global = nums[0]  # Initialize both variables with the first element of the array

        for num in nums[1:]:
            # Update max_current to be the maximum of current element and the sum so far
            max_current = max(num, max_current + num)
            
            # Update max_global if max_current is greater
            max_global = max(max_global, max_current)

        return max_global
            
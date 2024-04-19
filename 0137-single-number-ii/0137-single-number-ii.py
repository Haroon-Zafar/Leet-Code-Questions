class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_count = {}
        for num in nums:
            if num not in nums_count:
                nums_count[num] = 1
            else :
                nums_count[num] += 1
                
        for key in nums_count :
            if (nums_count[key] == 1) :
                return (key)
        
        
        
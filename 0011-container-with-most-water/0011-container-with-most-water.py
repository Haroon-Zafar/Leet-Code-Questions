class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate the area between the two pointers
            current_height = height[left] if height[left] < height[right] else height[right]
            current_width = right - left
            current_area = current_height * current_width
            
            # Update max_area if the current area is greater
            if current_area > max_area:
                max_area = current_area
            
            # Move the pointer with the smaller height towards the center
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
            
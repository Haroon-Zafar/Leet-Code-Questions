class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        len_of_str = len(s)
        prev_count = 1
        prev_prev_count = 0
        
        for index in range(len_of_str):
            current_count = 0
            
            # Single-digit decoding
            if s[index] != '0':
                current_count += prev_count
            
            # Two-digit decoding
            if index > 0 and (s[index - 1] == '1' or (s[index - 1] == '2' and s[index] <= '6')):
                current_count += prev_prev_count
            
            # Update counts for the next iteration
            prev_prev_count = prev_count
            prev_count = current_count
            
        return prev_count
                    
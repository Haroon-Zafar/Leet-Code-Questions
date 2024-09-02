class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        if not string:
            return 0
        
        unique = []
        max_length = 0

        for char in string:
            if char not in unique:
                unique.append(char)
                if len(unique) > max_length:
                    max_length = len(unique)
                
            else:
                unique = unique[unique.index(char)+1:]
                unique.append(char)
        return (max_length)
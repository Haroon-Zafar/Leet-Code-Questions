class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for char in range(len(haystack)-len(needle)+1):
            if (haystack[char:char+len(needle)] == needle):
                return (char)
        return(-1)


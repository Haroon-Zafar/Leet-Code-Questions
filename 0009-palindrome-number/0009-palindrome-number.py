class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrome = str(x)
        return (palindrome[0:] == palindrome[::-1])
        
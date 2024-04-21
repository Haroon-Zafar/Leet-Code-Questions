class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)
            if n == 1 :
                return (True)
        return False

    def sumOfSquares(self, num):
        output = 0
        while num :
            digit = num % 10
            digit = digit ** 2
            output += digit
            num = num // 10

        return (output)


        
        
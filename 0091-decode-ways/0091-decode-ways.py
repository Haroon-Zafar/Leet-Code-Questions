class Solution:
    def numDecodings(self, s: str) -> int:
        count, single_digit, double_digit = 0, 1, 0
        for i in range(len(s) -1, -1, -1):
            if s[i] != "0":
                count += single_digit
            if (s[i] == "1") or ((i + 1 < len(s)) and (s[i] == "2") and (int(s[i+1]) <= 6 )):
                count += double_digit
            double_digit = single_digit
            single_digit = count
            count = 0
        return single_digit
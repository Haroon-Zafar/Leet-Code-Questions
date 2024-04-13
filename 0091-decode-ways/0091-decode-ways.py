class Solution:
    def numDecodings(self, s: str) -> int:
        c, c1, c2 = 0, 1, 0
        for i in range(len(s) -1, -1, -1):
            if s[i] != "0":
                c += c1
            if (s[i] == "1") or ((i + 1 < len(s)) and (s[i] == "2") and (s[i+1] in "0123456" )):
                c += c2
            c2 = c1
            c1 = c
            c = 0
        return c1
class Solution:
    def reverseDegree(self, s: str) -> int:
        index = 1
        ans = 0
        for c in s:
            alphabetValue = 123 - ord(c)
            ans += alphabetValue*index
            index+=1

        return ans


x = Solution()
x.reverseDegree("zaza")

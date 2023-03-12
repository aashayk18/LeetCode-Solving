class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        num = str(bin(n)[2:])
        for i in range (len(num)):
            for j in range (i + 1, len(num)):
                if num[i] == '1' and num[j] == '1':
                    ans = max(ans, j - i)
                    break
        return ans

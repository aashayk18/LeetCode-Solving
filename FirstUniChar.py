class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,j in collections.Counter(s).items():
            if j == 1: return s.index(i)
        return -1
import numpy as np
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = sum(nums)
        b = sum(set(nums))
        c = (n*(n+1))//2
        return [a-b,c-b]
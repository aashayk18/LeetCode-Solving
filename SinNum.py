class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       return functools.reduce(operator.ixor,nums)
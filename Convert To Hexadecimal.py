class Solution:
    def toHex(self, num: int) -> str:
        return "{0:x}".format(num) if num >= 0 else "{0:x}".format(2**32 + num)

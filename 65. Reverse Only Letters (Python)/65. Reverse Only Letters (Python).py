class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = []
        for a in s:
            if a.isalpha() : l.append(a)
        l = l [::-1]

        for i, c in enumerate(s):
            if not c.isalpha():
                l.insert(i, c)

        return "".join(l)

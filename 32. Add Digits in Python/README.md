# Intuition
Add digits of the number by iterating over the number string.

# Approach
Since for all numbers less than 10, the sum of the digits will just be the number itself, we set a condition for the number being greater than or equal to 10. Then, we convert the number into a string using the in-built `str()` function in Python. We then iterate over this string using the variable `i` to denote each individual character, and convert `i` to an integer. We pass each character of the string in this manner to the in-built `sum()` function and store the result in `num` itself. Finally, we return the value of `num`, which is the sum of the digits of the number.
# Complexity
- Time complexity:


- Space complexity:

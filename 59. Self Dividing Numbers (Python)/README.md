# Intuition
Check if the number contains 0 or if the number is divisible by any of its digits, and it to an array of valid numbers.

# Approach
Define a function `div(n)` that takes an integer as an input and converts it to a string using the `str()` function. It then iterates over this string to check if each character i.e. each digit of the integer, is 0. It also checks if the integer is not divisible by each digit (i.e. the integer form of the character obtained by using the `int()` method). If either of the conditions is satisfiedm, the function returns false. Otherwise, it returns true by default. Initialize an empty array `ans`. Iterate over the integers in the range of `left` to `right`, and check if the `div()` function returns true for any integer. If it does, append that value to the `ans` array. Finally, return the `ans` array. 

# Complexity
- Time complexity:


- Space complexity:

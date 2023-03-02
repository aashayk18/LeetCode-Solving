# Intuition
Get the sum of all the 1's in the binary representation of the number for all the numbers in the given range.

# Approach
For the given range of `(n+1)`, convert each number to its binary representation by using the `bin()` function. Omit the `"0b"` characters from this binary representation by splicing the string using `[2:]`. Run a `map()` function over this binary representation to convert it into an integer array from a string. Run the sum() function over this integer array to get the sum of all the `1's` in the binary representation (since the sum would be a sum of all the 1's and 0's i.e. the sum of the 1's). Return an array version of this.

# Complexity
- Time complexity:


- Space complexity:

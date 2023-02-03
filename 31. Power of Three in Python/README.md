# Intuition
Check for a non-zero integer that perfectly divides the largest power of 3 in the given range.

# Approach
Check if n is greater than 0. Then, check if n perfectly divides the highest power of 3 in the given range of `-2^31` to `(2^31)-1` i.e. `3^19` or 1162261467. Return the boolean value for this expression.

# Complexity
- Time complexity:


- Space complexity:

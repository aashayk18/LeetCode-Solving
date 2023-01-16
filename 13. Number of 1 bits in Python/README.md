# Intuition
Perform binary bitwise operations to get the count of 1's.

# Approach
Initialize a count variable as 0. Run a while loop for when there still are digits left in the input. Perform the bitwise AND operation with n and (n-1), as this operation removes the rightmost 1 in a binary number. For example, 1011 & 1001 = 100. With each AND operation, increase the count by 1. Finally, return the count.

# Complexity
- Time complexity:


- Space complexity:

# Intuition
Binary 'OR' will give 1 where bits are different, and the count of 1's will reveal the number of times it happens.

# Approach
Perform the bitwise 'OR' operation on x and y. Convert this result into a binary string using `bin()` function and use the `count()` function to count the number of 1's to find the number of times the bits are different. Return this value as the required Hamming distance.

# Complexity
- Time complexity:


- Space complexity:

# Intuition
Identify the powers of 4 by performing binary operations and validating the results.

# Approach
Similar to the [Power of Two](https://leetcode.com/problems/power-of-two/solutions/3126710/power-of-two-in-python/) solution logic, we perform binary 'AND' operation tofind out whether a number is the power of 2. We then check an additional condition - whether the value of (n-1) is divisible by 3 or not. This means that if (n-1) is divisible by 3, then n is divisible by 4. Which differentiates the powers of 4 from the powers of 2 we earlier found out. We return the boolean value for this expression as our final result.

# Complexity
- Time complexity:


- Space complexity:

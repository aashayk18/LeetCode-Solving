# Intuition
Find the difference between the sum of expected elements and sum of actual elements.

# Approach
Use the `sum()` function to calculate the sum of all the numbers leading up to one more than the total length of the `nums` array. This gives us the sum of all the expected elements, since it also includes the missing element. This is because the numbers are all the consecutive numbers in the range (0,n). Next, calculate the sum of all the elements in ths `nums` array. Subtract the second value from the first, to obtain the missing number. Return this number.

# Complexity
- Time complexity:
$O(N)$

- Space complexity:
$O(1)$

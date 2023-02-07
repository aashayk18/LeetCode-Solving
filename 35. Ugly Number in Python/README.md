# Intuition
Divide the number by 2,3, and 5 to see if they are its factors.

# Approach
Check if n is smaller than 0, if so, return false. Define a list of factors that contains 2,3, and 5. Iterate over the list, and check if the modulus of n when divided by each number is 0 or not. Run a while loop, that if the condition is met, n becomes equal to the result of its floor division by a factor. This way, we understand if a number only has 2,3, and 5 as its prime factors. Finally, we check if n has become 1 after being divided by all its factors. We return the boolean value for this expression.


# Complexity
- Time complexity:
$O(log(N))$

- Space complexity:
$O(1)$

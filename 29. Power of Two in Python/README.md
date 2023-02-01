# Intuition
Use binary bit operations to check whether a number is the power of 2 or not.

# Approach
Check if n is 0, and if so, return False. Otherwise, return the boolean value of the expression n & n-1.

Here, 
$n$ represents the binary value of the input number
$n-1$ represents the binary value of the number lesser than n
$&$ represents the binary 'AND' operation

All the numbers that are a power of two will have only one, '1' bit and rest '0' bits in their binary representation. Similarly, the numbers less than a power of two will have only one '0' bit (in the exact same position as the '1' bit in n) and rest '1' bits (in the exact same position as the '0' bits in n) in their binary representation. Performing the binary 'AND' operation on these two numbers will therefore give the result as 0.

Let us understand with the help of an example.

- n = 8

Here, the binary representation of n is given by '1000'.
Similarly, the binary representation of n-1 is given by '0111'.

Let us perform the binary 'AND' operation on these two numbers.

1000            
0111            ---------> Since all of the bits complement each other, we get the result as '0000'.
-_-_-_-_-_-_
0000 ---------> This equates to decimal 0.

This can be observed with any such number that is a power of two, so we accept it as a condition for our expression.

# Complexity
- Time complexity: $$O(1)$$

- Space complexity: $$O(1)$$

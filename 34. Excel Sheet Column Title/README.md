# Intuition
Assign characters as per unicode values, keeping in mind the values that go beyond the 26 letters of the alphabet.

# Approach
Assign the value of `columnNumber` to a variable `n`. Initialize a blank string `res`. Initialize a while loop with the condition `n > 0`. 
Inside the `while loop`:
Decrement the value of `n` by 1, to fit the number system starting with `0` instead of `1`. Calculate the modulus of `n` when divided by `26`, to get the value by which the number is exceeding the 26 letters of the alphabet. Add this value to the unicode value of `A`, to get the unicode value of the letter. Apply the `chr` function with this value as the input, to get the letter. Concatenate this with the string `res`. Calculate the value of the floor division of `n` by 26, to move on to the next value for consideration in the loop.

**Let us understand this with the help of an example:**

Suppose, `columnNumber` is given as 27.
We assign this value to `n`.
Then initialize the empty string `res`.
Check the while loop codition, which is passed. So, we enter the loop. 
Decrement `n` by 1, so we get 26. 
Next, the modulus of `n` when divided by 26 is calculated as 0. We add this to the unicode value of `A`, which gives us 65. 
The `chr` function returns `A` for this value. 
We concatenate `A` with res, to get `A`.
Floor division of `n` by 26 gives 1.
This value goes back into the loop. 
The condition is passed, so we wnter the loop and `n` is decremented to 0. 
The modulus is still 0, so the output of `chr` function is `A`, which is concatenated with the previous value of `res`, which is `A`.
Floor division of `n` by 26 now gives 0, which fails the loop condition, so we exit.
Finally, we return the value of `res` as `AA`.

# Complexity
- Time complexity:


- Space complexity:

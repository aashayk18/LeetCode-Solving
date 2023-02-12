# Intuition
Iterate over both strings to find out whether the elements of the first are present in the second or not.

# Approach
Initialize variables `i` and `j` as 0. Run a while loop with two conditions that `i` is less than the length of `s` and that `j` is less than the length of `t`. Iterate over the two strings now to check if the elements of `s` match the elements of `t`. If there's a match, increment `i` by 1 to move the pointer to the next character in `s`. Increment `j` as well, with each step of the loop to traverse `t`. At the end, check if `i` has become equal to the length of `s`. This will tell us if we found all the elements of `s` in `t`. Return the boolean value for this expression.

# Complexity
- Time complexity:


- Space complexity:

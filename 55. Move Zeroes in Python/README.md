# Intuition
Check if the element is a 0, if not then swap it with the previous element in order to move all the non-zero elements to the start of the array.

# Approach
Initialize a variable `i` to 0. Iterate over the length of the `nums` array using a variable `j`. If the j'th element of the array is non-zero, swap the `i'th` element of the array with the `j'th` element. Increment `i` by 1. This way, all the non-zero elements of the array are moved to the start of the array, while all the zeroes are pushed to the end.

# Complexity
- Time complexity:


- Space complexity:
